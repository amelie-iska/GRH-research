"""Candidate C: digital IQ integration, affine discrimination and steering.

Synthetic integer samples only. No device, pulse, credential or network access.
Feature sums use a proven bounded accumulator; score compares at W+F scale.
The output is an action REQUEST, never an executable instrument instruction.
"""
from dataclasses import dataclass
from fixed import Format


@dataclass(frozen=True)
class Calibration:
    epoch: int
    wi: int
    wq: int
    bias: int
    threshold: int
    margin: int
    action_above: str = "RESET_REQUEST"


class ReadoutController:
    def __init__(self, calibration, fmt=Format(), max_samples=16,
                 decision_latency=3):
        if type(max_samples) is not int or max_samples < 1:
            raise ValueError("positive sample capacity required")
        if type(decision_latency) is not int or decision_latency < 1:
            raise ValueError("positive decision latency required")
        for raw in (calibration.wi, calibration.wq, calibration.bias,
                    calibration.threshold, calibration.margin):
            fmt.check(raw)
        if calibration.margin < 0 or calibration.epoch < 0:
            raise ValueError("nonnegative epoch and margin required")
        if calibration.action_above not in ("RESET_REQUEST", "X_REQUEST"):
            raise ValueError("action outside explicit allowlist")
        self.cal, self.fmt, self.max_samples = calibration, fmt, max_samples
        self.decision_latency = decision_latency
        # ceil(log2 N), including N=1, suffices for N signed W-bit samples.
        self.acc_width = fmt.width + (max_samples - 1).bit_length()

    def decide(self, samples, frame_epoch, end_cycle, deadline):
        si, sq, count, overrun = 0, 0, 0, False
        for i, q, valid in samples:
            self.fmt.check(i)
            self.fmt.check(q)
            if type(valid) is not bool:
                raise ValueError("sample valid must be bool")
            if valid:
                count += 1
                if count <= self.max_samples:
                    si += i
                    sq += q
                else:
                    overrun = True
        # Products are W+acc_width bits; one guard bit for the two products,
        # plus a bias at the same scale. Python represents that exact integer.
        score_wide = si * self.cal.wi + sq * self.cal.wq
        score_wide += self.cal.bias << self.fmt.frac
        score, overflow = self.fmt.sat(score_wide >> self.fmt.frac)
        delta = score - self.cal.threshold
        reasons = []
        if count == 0:
            reasons.append("empty_frame")
        if overrun:
            reasons.append("sample_overrun")
        if frame_epoch != self.cal.epoch:
            reasons.append("stale_calibration")
        if overflow:
            reasons.append("score_saturated")
        if abs(delta) < self.cal.margin:
            reasons.append("low_margin")
        if end_cycle + self.decision_latency > deadline:
            reasons.append("deadline_miss")
        valid = not reasons
        return {"sum_i": si, "sum_q": sq, "samples": count,
                "acc_width": self.acc_width, "score_raw": score,
                "score_wide": score_wide, "overflow": overflow,
                "valid": valid, "reasons": reasons,
                "decision_cycle": end_cycle + self.decision_latency,
                "action": self.cal.action_above if valid and delta > 0 else "HOLD"}


if __name__ == "__main__":
    controller = ReadoutController(Calibration(1, 8, -4, 0, 0, 2))
    print(controller.decide([(8, 0, True)] * 4, 1, 20, 25))
