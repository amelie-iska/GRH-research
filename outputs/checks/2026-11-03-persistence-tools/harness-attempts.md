# Preserved diagnostic attempts

The first standalone/browser run passed the algebra/quantum controls, then
failed the book readiness predicate because iframe.contentDocument existed
while its body was null. The predicate now checks body with optional chaining;
this is a harness correction, not a change to the numerical model.

A later isolated Chrome profile stopped responding to CDP, including its own
Browser.close request and /json/version. Its cause was not established. Only
that known test process was terminated with SIGTERM; no user browser, preview,
profile, source or cache was removed. The launcher refused a launch while
that test port was still occupied. Fresh-profile final persistence, companion
and 22-case architecture browser regressions passed. Raw profile logs and
all profiles are preserved under ignored outputs/browser-tests. Recorded
attempt logs remain beside the final checks where available. No mathematical
claim depends on a failed browser attempt.
