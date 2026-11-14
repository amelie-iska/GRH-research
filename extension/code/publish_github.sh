#!/usr/bin/env bash
# Publish this reviewed clone after ordinary GitHub CLI authentication.
# Publish to the existing user-authorized GRH repository without a force push.
set -euo pipefail

project_root=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)
cd -- "$project_root"
target='amelie-iska/GRH-research'
https_remote="https://github.com/${target}.git"
ssh_remote="git@github.com:${target}.git"

if [[ -n $(git status --porcelain) ]]; then
  printf '%s\n' 'Commit the reviewed source tree before publishing.' >&2
  exit 1
fi
gh auth status --hostname github.com
account=$(gh api user --jq .login)
if [[ "$account" != 'amelie-iska' ]]; then
  printf '%s\n' 'The authenticated account must be amelie-iska.' >&2
  exit 1
fi
gh repo view "$target" --json nameWithOwner,viewerPermission

if existing_remote=$(git remote get-url origin 2>/dev/null); then
  if [[ "${existing_remote,,}" != "${https_remote,,}" && "${existing_remote,,}" != "${ssh_remote,,}" ]]; then
    printf '%s\n' 'origin points elsewhere; inspect it before publishing.' >&2
    exit 1
  fi
else
  git remote add origin "$https_remote"
fi

git fetch origin refs/heads/main:refs/remotes/origin/main
if ! git merge-base --is-ancestor origin/main HEAD; then
  printf '%s\n' 'The published main branch has changes not in HEAD. Integrate them before publishing.' >&2
  exit 1
fi
git push --set-upstream origin HEAD:refs/heads/main
local_commit=$(git rev-parse HEAD)
remote_commit=$(git ls-remote --heads origin refs/heads/main | cut -f1)
if [[ "$local_commit" != "$remote_commit" ]]; then
  printf '%s\n' 'Published branch verification failed; inspect without force pushing.' >&2
  exit 1
fi
gh repo view "$target" --json url,isPrivate,defaultBranchRef
printf 'Verified published commit: %s\n' "$local_commit"
