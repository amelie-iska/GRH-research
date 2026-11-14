#!/usr/bin/env python3
"""Separate, bounded GPU capacity followup to the immutable original run.

Run one GPU experiment process at a time. This script never changes the
original gpu_experiments.py or gpu-results.json. Its largest test is specific
to Pauli frames, the fixed shot count, and the observed free-memory budget;
it does not establish an absolute or state-vector qubit capacity.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import time
import traceback

import cupy as cp
from gpu_experiments import HERE, RESERVE, environment, frame_case


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def utc_now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def provenance():
    paths = [HERE / 'gpu_capacity.py', HERE / 'gpu_experiments.py',
             HERE / 'surface_codes.py']
    paths.extend(sorted((HERE / 'cases').glob('*.json')))
    original = HERE / 'results' / 'gpu-results.json'
    if original.exists():
        paths.append(original)
    return {str(p.relative_to(HERE)): {'sha256': sha256(p), 'bytes': p.stat().st_size}
            for p in paths}


def select_lattice(shots, multiple=32):
    """Use an integer calculation for the 5/4 overhead memory inequality."""
    free, total = cp.cuda.runtime.memGetInfo()
    stride = ((shots + 31) // 32) * 4
    available = max(0, free - RESERVE)
    # Square torus: data=2L^2, ancilla=2L^2, total=4L^2.
    # X and Z frame bits plus ancilla measurement bits: 10L^2*stride.
    limit = math.isqrt((4 * available) // (5 * 10 * stride))
    lattice = (limit // multiple) * multiple
    if lattice < 32:
        raise MemoryError('The fixed reserve and overhead leave no supported capacity test')
    estimated = 10 * lattice * lattice * stride
    return {'lattice_size': lattice, 'rounding_multiple': multiple,
            'shots': shots, 'packed_bytes_per_qubit': stride,
            'free_bytes_at_selection': free, 'total_device_bytes': total,
            'fixed_reserve_bytes': RESERVE, 'overhead_factor': 1.25,
            'estimated_bit_table_bytes': estimated,
            'estimated_required_bytes_including_overhead_and_reserve':
                (5 * estimated + 3) // 4 + RESERVE,
            'selection_rule': 'largest multiple of 32 with 1.25*(10*L^2*stride) <= free-2GiB',
            'claim_limit': 'Bounded test at this shot count and representation, not an absolute qubit maximum'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=HERE / 'results' / 'capacity-results.json')
    parser.add_argument('--shots', type=int, default=32768)
    args = parser.parse_args()
    if args.shots != 32768:
        raise ValueError('This recorded followup fixes the comparison at 32768 shots')
    if args.output.resolve() == (HERE / 'results' / 'gpu-results.json').resolve():
        raise ValueError('The original GPU evidence file cannot be overwritten')
    if args.output.exists():
        raise FileExistsError('Use a new --output path to preserve an existing capacity record')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    result = {'schema_version': 1, 'mode': 'separate_capacity_followup',
              'environment': environment(), 'utc_started': utc_now(),
              'input_hashes': provenance(), 'experiments': [],
              'seed': 20261113, 'shots_per_experiment': args.shots,
              'library_search_path': os.environ.get('LD_LIBRARY_PATH', ''),
              'claim_limit': 'Pauli-error frames relative to an assumed ideal encoded CSS reference; no dense amplitudes or learned decoder'}

    def save():
        temporary = args.output.with_suffix(args.output.suffix + '.tmp')
        temporary.write_text(json.dumps(result, indent=2) + '\n')
        temporary.replace(args.output)

    def record(name, function):
        print('Running ' + name, flush=True)
        started = time.perf_counter()
        try:
            value = function()
            value['call_wall_seconds_including_topology_and_cleanup'] = time.perf_counter() - started
            result['experiments'].append({'name': name, **value})
            save()
            print(json.dumps({key: value[key] for key in
                              ['case', 'data_qubits', 'ancilla_qubits', 'total_qubits',
                               'shots', 'simulation_seconds', 'passed', 'status']
                              if key in value}), flush=True)
        except Exception as error:
            result['experiments'].append({'name': name, 'passed': False,
                                          'error': str(error), 'traceback': traceback.format_exc()})
            result['passed'] = False
            result['utc_finished'] = utc_now()
            save()
            raise

    save()
    record('genus3_frames', lambda: frame_case(name='genus3_3x3', shots=args.shots))
    result['capacity_selection'] = select_lattice(args.shots)
    size = result['capacity_selection']['lattice_size']
    save()
    record(f'torus_{size}_frames', lambda: frame_case(lattice_size=size, shots=args.shots))
    result['utc_finished'] = utc_now()
    result['passed'] = all(row.get('passed') is True for row in result['experiments'])
    result['input_hashes_unchanged'] = provenance() == result['input_hashes']
    if not result['input_hashes_unchanged']:
        result['passed'] = False
    save()
    print('Wrote ' + str(args.output), flush=True)


if __name__ == '__main__':
    main()
