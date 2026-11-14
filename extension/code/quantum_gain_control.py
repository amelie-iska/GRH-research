#!/usr/bin/env python3
"""Exact finite qubit channels with a nonlinear classical feedback controller.

The state domain is a tuple of separately accessible qubit ensemble density
matrices, represented by rational Bloch vectors. For each fixed control u,
rho -> a*rho + (1-a)*(I+u*Z)/2 is a CPTP identity/replacement channel when
0 <= a <= 1 and -1 <= u <= 1. The controller reads known ensemble Z
expectations, so the complete state-dependent update is nonlinear. It is not
a deterministic single-copy quantum channel on an unknown joint state.

This standard-library implementation is an exact classical simulation. It
contains no training, hardware execution, finite-shot instrument, fluid
solver or claim of quantum computational advantage. The optional readout
errors are deterministic bounded approximations, not measurement backaction.
"""
from __future__ import annotations

from fractions import Fraction as Q


RETENTION = Q(1, 4)
GRAPH = ((Q(0), Q(2)), (Q(1, 8), Q(0)))
BIAS = (Q(1, 4), Q(0))
WEIGHTS = (Q(4), Q(1))
RATE = Q(5, 8)
FIXED_POINT = ((Q(0), Q(0), Q(1, 3)), (Q(0), Q(0), Q(1, 24)))
INITIAL_STATE = ((Q(0), Q(1), Q(0)), (Q(0), Q(0), Q(-1)))
INITIAL_ERROR_BUDGET = Q(25, 48)


def exact_scalar(value, label="value"):
    if type(value) is not int and type(value) is not Q:
        raise TypeError(f"{label} must be a built-in int or fractions.Fraction")
    return Q(value)


def _vector(values, size, label):
    if type(values) not in (list, tuple) or len(values) != size:
        raise ValueError(f"{label} must have exactly {size} entries")
    return tuple(exact_scalar(value, f"{label}[{i}]") for i, value in enumerate(values))


def validate_bloch(state):
    """Return exact coordinates of a positive, trace-one qubit state."""
    state = _vector(state, 3, "Bloch state")
    if sum(value * value for value in state) > 1:
        raise ValueError("Bloch coordinates must lie in the closed unit ball")
    return state


def _states(states):
    if type(states) not in (list, tuple) or not states:
        raise ValueError("At least one separately accessible state block is required")
    return tuple(validate_bloch(state) for state in states)


def _graph(graph, size):
    if type(graph) not in (list, tuple) or len(graph) != size:
        raise ValueError("Controller graph must match the state-block dimension")
    return tuple(_vector(row, size, f"graph[{i}]") for i, row in enumerate(graph))


def _retention(value):
    value = exact_scalar(value, "retention")
    if not 0 <= value <= 1:
        raise ValueError("Retention must lie in [0,1]")
    return value


def clip_control(value):
    value = exact_scalar(value, "control argument")
    return min(Q(1), max(Q(-1), value))


def _control(value):
    value = exact_scalar(value, "fixed control")
    if not -1 <= value <= 1:
        raise ValueError("A fixed channel control must lie in [-1,1]")
    return value


def channel_step(state, control, retention=RETENTION):
    """Apply the fixed-control CPTP block in exact Bloch coordinates."""
    x, y, z = validate_bloch(state)
    u, a = _control(control), _retention(retention)
    return validate_bloch((a * x, a * y, a * z + (1 - a) * u))


def channel_choi(control, retention=RETENTION):
    """Unnormalized Choi matrix in input-tensor-output basis order.

    The trace is two and partial trace over the output equals the input
    identity. The returned entries are rational; no square root is evaluated.
    """
    u, a = _control(control), _retention(retention)
    c0, c1 = (1 - a) * (1 + u) / 2, (1 - a) * (1 - u) / 2
    zero = Q(0)
    return ((a + c0, zero, zero, a), (zero, c1, zero, zero),
            (zero, zero, c0, zero), (a, zero, zero, a + c1))


def choi_psd_decomposition(control, retention=RETENTION):
    """Nonnegative rational coefficients times rational rank-one forms.

    Each term c*v*v^T is positive semidefinite when c >= 0. This is an exact
    PSD witness without representing the generally irrational sqrt(c).
    """
    u, a = _control(control), _retention(retention)
    c0, c1 = (1 - a) * (1 + u) / 2, (1 - a) * (1 - u) / 2
    return ((a, (1, 0, 0, 1)), (c0, (1, 0, 0, 0)),
            (c1, (0, 1, 0, 0)), (c0, (0, 0, 1, 0)), (c1, (0, 0, 0, 1)))


def feedback_step(states, *, graph=GRAPH, bias=BIAS, retention=RETENTION,
                  measurement_errors=None):
    """Apply classical clipped feedback to separately accessible ensembles.

    Optional exact errors perturb the known Z expectations before the
    controller. The controller clips its final signal to [-1,1], so every
    chosen fixed-control block remains a valid channel. An error bound is
    an external assumption; this function does not infer one from data.
    """
    states = _states(states)
    size = len(states)
    graph, bias, a = _graph(graph, size), _vector(bias, size, "bias"), _retention(retention)
    errors = ((Q(0),) * size if measurement_errors is None
              else _vector(measurement_errors, size, "measurement errors"))
    readouts = tuple(state[2] + error for state, error in zip(states, errors))
    raw = tuple(sum(gain * value for gain, value in zip(row, readouts)) + offset
                for row, offset in zip(graph, bias))
    controls = tuple(clip_control(value) for value in raw)
    return {"states": tuple(channel_step(state, control, a)
                            for state, control in zip(states, controls)),
            "readouts": readouts, "raw_controls": raw, "controls": controls,
            "saturated": tuple(value != control for value, control in zip(raw, controls))}


def feedback_gain(*, graph=GRAPH, retention=RETENTION):
    """Global trace-distance envelope from clip's unit Lipschitz bound.

    G_ij = a*delta_ij + (1-a)*abs(B_ij). Its application uses
    |Tr(Z(rho-sigma))| <= 2*D(rho,sigma) and D(tau(u),tau(v))=|u-v|/2.
    Graph edges therefore encode classical controller gains, not quantum
    channel compositions or gentle-algebra zero relations.
    """
    if type(graph) not in (list, tuple) or not graph:
        raise ValueError("Controller graph must be nonempty")
    graph, a = _graph(graph, len(graph)), _retention(retention)
    return tuple(tuple(a * (i == j) + (1 - a) * abs(value)
                       for j, value in enumerate(row)) for i, row in enumerate(graph))


def squared_trace_distance(left, right):
    """Exact square of qubit trace distance, avoiding irrational roots."""
    left, right = validate_bloch(left), validate_bloch(right)
    return sum((a - b) ** 2 for a, b in zip(left, right)) / 4


def readout_error_budget(error_bounds, *, graph=GRAPH, weights=WEIGHTS, retention=RETENTION):
    """A weighted one-step budget conditional on the supplied readout errors.

    delta = max_i (1-a)/(2*w_i) * sum_j abs(B_ij)*epsilon_j.
    No probabilistic, finite-shot, tomography or device-noise claim is made.
    """
    if type(graph) not in (list, tuple) or not graph:
        raise ValueError("Controller graph must be nonempty")
    size = len(graph)
    graph, a = _graph(graph, size), _retention(retention)
    errors = _vector(error_bounds, size, "readout error bounds")
    weights = _vector(weights, size, "weights")
    if any(error < 0 for error in errors) or any(weight <= 0 for weight in weights):
        raise ValueError("Error bounds must be nonnegative and weights strictly positive")
    return max((1 - a) * sum(abs(gain) * error for gain, error in zip(row, errors)) / (2 * weight)
               for row, weight in zip(graph, weights))


def iterate_error_budget(rate, initial, residuals):
    """Exact recurrence r_{n+1}=q*r_n+delta_n, including q >= 1."""
    rate, initial = exact_scalar(rate, "rate"), exact_scalar(initial, "initial budget")
    if rate < 0 or initial < 0:
        raise ValueError("Rate and initial budget must be nonnegative")
    if type(residuals) not in (list, tuple):
        raise ValueError("Residuals must be a finite list or tuple")
    residuals = tuple(exact_scalar(value, "residual") for value in residuals)
    if any(value < 0 for value in residuals):
        raise ValueError("Residual budgets must be nonnegative")
    budgets = [initial]
    for residual in residuals:
        budgets.append(rate * budgets[-1] + residual)
    return tuple(budgets)


def encode_exact(value):
    """Encode rationals with decimal strings, retaining JSON metadata types."""
    if type(value) is Q:
        return {"numerator": str(value.numerator), "denominator": str(value.denominator)}
    if type(value) in (int, bool, str) or value is None:
        return value
    if type(value) in (list, tuple):
        return [encode_exact(item) for item in value]
    if type(value) is dict and all(type(key) is str for key in value):
        return {key: encode_exact(item) for key, item in value.items()}
    raise TypeError("Evidence values must be exact rationals, JSON metadata or finite containers")
