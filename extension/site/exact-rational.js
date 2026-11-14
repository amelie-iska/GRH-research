/* Exact rational arithmetic for certificate inputs. No floating-point coercion. */
(function (root) {
  'use strict';
  const MAX_DIGITS = 256;
  function gcd(a, b) { a = a < 0n ? -a : a; while (b) [a, b] = [b, a % b]; return a; }
  function make(n, d = 1n) {
    if (typeof n !== 'bigint' || typeof d !== 'bigint') throw new TypeError('Rational components must be BigInt.');
    if (!d) throw new RangeError('A rational denominator cannot be zero.');
    if (d < 0n) { n = -n; d = -d; }
    const g = gcd(n, d);
    return Object.freeze({n: n / g, d: d / g});
  }
  function parse(text) {
    if (typeof text !== 'string' || text.length > 2 * MAX_DIGITS + 2 || !/^(0|-[1-9][0-9]*|[1-9][0-9]*)\/[1-9][0-9]*$/.test(text))
      throw new TypeError('Use a reduced canonical rational string n/d with positive denominator.');
    const [n, d] = text.split('/');
    if (n.replace('-', '').length > MAX_DIGITS || d.length > MAX_DIGITS) throw new RangeError('Rational input exceeds the digit limit.');
    const r = make(BigInt(n), BigInt(d));
    if (format(r) !== text) throw new TypeError('Rational input is not reduced.');
    return r;
  }
  const format = r => `${r.n}/${r.d}`;
  const add = (a, b) => make(a.n * b.d + b.n * a.d, a.d * b.d);
  const sub = (a, b) => make(a.n * b.d - b.n * a.d, a.d * b.d);
  const mul = (a, b) => make(a.n * b.n, a.d * b.d);
  const div = (a, b) => make(a.n * b.d, a.d * b.n);
  const neg = a => make(-a.n, a.d);
  const cmp = (a, b) => { const d = a.n * b.d - b.n * a.d; return d < 0n ? -1 : d > 0n ? 1 : 0; };
  const equal = (a, b) => cmp(a, b) === 0;
  const floor = a => a.n >= 0n ? a.n / a.d : -((-a.n + a.d - 1n) / a.d);
  function pow(a, n) {
    if (!Number.isSafeInteger(n) || n < 0 || n > 256) throw new RangeError('Use a nonnegative integer exponent at most 256.');
    return make(a.n ** BigInt(n), a.d ** BigInt(n));
  }
  function fromDecimal(text) {
    if (typeof text !== 'string' || text.length > 260 || !/^-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:e[+-]?[0-9]+)?$/i.test(text))
      throw new TypeError('An exact decimal string is required.');
    const [coefficient, expText = '0'] = text.toLowerCase().split('e');
    const exponent = BigInt(expText);
    if (exponent < -256n || exponent > 256n) throw new RangeError('Decimal exponent exceeds the exact input limit.');
    const parts = coefficient.split('.'), digits = (parts[1] || '').length;
    let n = BigInt(parts[0] + (parts[1] || '')), d = 10n ** BigInt(digits);
    if (exponent >= 0n) n *= 10n ** exponent; else d *= 10n ** (-exponent);
    return make(n, d);
  }
  // Rendering only. Certificate comparisons use cmp and integer arithmetic.
  function toNumber(r) {
    if (!r.n) return 0;
    const negative = r.n < 0n, numerator = (negative ? -r.n : r.n).toString(), denominator = r.d.toString();
    const a = numerator.slice(0, 16), b = denominator.slice(0, 16);
    let mantissa = Number(a) / Number(b), exponent = (numerator.length - a.length) - (denominator.length - b.length);
    while (mantissa >= 10) { mantissa /= 10; exponent++; }
    while (mantissa < 1) { mantissa *= 10; exponent--; }
    // Parsing the whole scientific notation also handles subnormal rounding;
    // computing 10**exponent first would underflow prematurely at exponent -324.
    return Number(`${negative ? '-' : ''}${mantissa}e${exponent}`);
  }
  const api = Object.freeze({MAX_DIGITS, make, parse, format, add, sub, mul, div, neg, cmp, equal, pow, floor, fromDecimal, toNumber});
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  root.ExactRational = api;
})(typeof globalThis !== 'undefined' ? globalThis : this);
