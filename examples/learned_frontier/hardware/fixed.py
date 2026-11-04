"""Dependency-free integer contracts for candidate hardware, not an RTL simulator."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Format:
    width: int = 8
    frac: int = 4

    def __post_init__(self):
        if self.width < 2 or not 0 <= self.frac < self.width:
            raise ValueError("require width >= 2 and 0 <= frac < width")

    @property
    def lo(self):
        return -(1 << (self.width - 1))

    @property
    def hi(self):
        return (1 << (self.width - 1)) - 1

    def check(self, x):
        if type(x) is not int or not self.lo <= x <= self.hi:
            raise ValueError("raw signed integer outside format")
        return x

    def sat(self, x):
        return min(self.hi, max(self.lo, x)), not self.lo <= x <= self.hi

    def encode(self, x):
        return self.check(x) & ((1 << self.width) - 1)

    def decode(self, bits):
        if type(bits) is not int or not 0 <= bits < 1 << self.width:
            raise ValueError("invalid bit pattern")
        return bits - (1 << self.width) if bits >> (self.width - 1) else bits
