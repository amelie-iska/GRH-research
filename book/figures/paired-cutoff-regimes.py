#!/usr/bin/env python3
"""Draw the reviewed pure-cutoff regime map as editable SVG and vector PDF."""

import argparse
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from html import escape
import json
from math import cos, radians, sin
from pathlib import Path
from typing import Optional


F = Fraction
HERE = Path(__file__).resolve().parent
WIDTH, HEIGHT = 760, 558
LEFT, TOP, RIGHT, BOTTOM = 84, 98, 720, 417
B_MIN, B_MAX, K_MIN, K_MAX = F(13, 20), F(1), F(12, 25), F(21, 25)
A = F(3, 4)
LONG_INSERTION = F(1089, 1420)
LARGE_ERASURE = F(1355, 1482)
SHORT_INSERTION = F(921, 1652)
CENTRAL_SHORT_START = F(57, 80)
CENTRAL_LONG_START = F(273, 404)
PRODUCT_START = F(2, 3)
CENTRAL_LONG_JOIN = (2768 * LONG_INSERTION - 1743) / 508
SOURCES = {
    "planning/pure-intermediate-20261108/LONG_INSERTION_ALL_ERASURES-v1.md":
        "5de437e62878d96c05c01240df29a4dd3b97c4930f5db96fce13c2bddec75b75",
    "planning/pure-intermediate-20261108/INTERMEDIATE_ERASURE-v1.md":
        "2f17255a51fbe1be8bd695fe7cbc28be90f5beaab2921e5b8374b7bd80da473b",
    "planning/pure-intermediate-20261108/SHORT_INSERTION_ALL_LARGE_ERASURES-v1.md":
        "e9cd7dc765ce8d7c0852dd8927dd175c7eda6fc5e7b3a8c71e1625577bd3583e",
    "planning/pure-intermediate-20261108/CENTRAL_RECTANGLES-v1.md":
        "c936870a1fcae69471edff65a92efb3ac192db7cb2b3b90eef3a6582dfa4637e",
    "outputs/checks/2026-11-08-pure-intermediate/REVIEW-v1.json":
        "41ba3eb06125bcf169cf8b1de5367fa3406c90225139ff1fc277bc5d91544114",
}

TITLE = "Where the pure cross reaches the target"
SUBTITLE = "Selected original pure cross, summed over all intermediate divisors"
DESCRIPTION = (
    "Regime map for the selected original pure two-pivot cross at R of order "
    "D to the three quarters. The horizontal axis is b = log base D of B, "
    "the erased cutoff norm, and the vertical axis is k = log base D of K, "
    "the insertion norm. Solid fill marks proved normalized "
    "O(D to the three quarters plus epsilon) comparisons over all d. "
    "The broad thresholds are k at least 1089/1420 for every b, b at least "
    "1355/1482 for every k, and k at most 921/1652 for b at least 3/4. "
    "Dashed boundaries add reviewed affine central regions. The dotted "
    "boundary gives a conditional comparison below it when the fixed "
    "label product stays bounded. Unshaded cells remain open under the "
    "displayed comparisons. The map omits other label and divisor selectors "
    "and concerns neither the whole signed form nor a lower bound."
)

INK = "#142D39"
SECONDARY = "#314B56"
GRID = "#B9C8CA"
PLOT = "#FBF8EF"
FILL = "#D4E9E8"
BOUND = "#146563"
ACCENT = "#78395D"
GUIDE = "#527278"
WHITE = "#FFFFFF"

Point = tuple[float, float]


@dataclass(frozen=True)
class Shape:
    points: tuple[Point, ...]
    fill: Optional[str] = None
    stroke: Optional[str] = None
    width: float = 1.0
    dash: tuple[float, ...] = ()
    closed: bool = False


@dataclass(frozen=True)
class Label:
    x: float
    y: float
    value: str
    size: float
    color: str = INK
    bold: bool = False
    anchor: str = "start"
    angle: float = 0.0


def central_short(b: F) -> F:
    return (172 * b + 21) / 264


def central_long(b: F) -> F:
    return (508 * b + 1743) / 2768


def fixed_product(b: F) -> F:
    return (308 * b + 21) / 400


def map_point(b: F, k: F) -> Point:
    return (
        LEFT + float((b - B_MIN) / (B_MAX - B_MIN)) * (RIGHT - LEFT),
        BOTTOM - float((k - K_MIN) / (K_MAX - K_MIN)) * (BOTTOM - TOP),
    )


def line(x1: float, y1: float, x2: float, y2: float,
         stroke: str, width: float = 1.0, dash: tuple[float, ...] = ()) -> Shape:
    return Shape(((x1, y1), (x2, y2)), stroke=stroke, width=width, dash=dash)


def trace(points: tuple[tuple[F, F], ...], stroke: str, width: float,
          dash: tuple[float, ...] = ()) -> Shape:
    return Shape(tuple(map_point(*point) for point in points),
                 stroke=stroke, width=width, dash=dash)


def area(points: tuple[tuple[F, F], ...], fill: str) -> Shape:
    return Shape(tuple(map_point(*point) for point in points), fill=fill, closed=True)


def rectangle(x: float, y: float, width: float, height: float,
              fill: Optional[str] = None, stroke: Optional[str] = None,
              line_width: float = 1.0) -> Shape:
    return Shape(((x, y), (x + width, y), (x + width, y + height), (x, y + height)),
                 fill=fill, stroke=stroke, width=line_width, closed=True)


def make_scene() -> list[Shape | Label]:
    scene: list[Shape | Label] = [
        rectangle(0, 0, WIDTH, HEIGHT, WHITE),
        Label(LEFT, 42, TITLE, 27, bold=True),
        Label(LEFT, 67, SUBTITLE, 16, SECONDARY),
        rectangle(LEFT, TOP, RIGHT - LEFT, BOTTOM - TOP, PLOT),
        area(((B_MIN, LONG_INSERTION), (B_MAX, LONG_INSERTION),
              (B_MAX, K_MAX), (B_MIN, K_MAX)), FILL),
        area(((LARGE_ERASURE, K_MIN), (B_MAX, K_MIN),
              (B_MAX, K_MAX), (LARGE_ERASURE, K_MAX)), FILL),
        area(((A, K_MIN), (LARGE_ERASURE, K_MIN),
              (LARGE_ERASURE, SHORT_INSERTION), (A, SHORT_INSERTION)), FILL),
        area(((CENTRAL_SHORT_START, K_MIN), (A, K_MIN),
              (A, central_short(A)), (CENTRAL_SHORT_START, central_short(CENTRAL_SHORT_START))), FILL),
        area(((CENTRAL_LONG_START, central_long(CENTRAL_LONG_START)),
              (CENTRAL_LONG_JOIN, LONG_INSERTION), (CENTRAL_LONG_START, LONG_INSERTION)), FILL),
    ]
    b_ticks = tuple(F(t, 100) for t in range(65, 101, 5))
    k_ticks = tuple(F(t, 100) for t in range(48, 85, 6))
    for b in b_ticks:
        x, _ = map_point(b, K_MIN)
        scene += [
            line(x, TOP, x, BOTTOM, GRID, 0.75),
            line(x, BOTTOM, x, BOTTOM + 5, SECONDARY, 1.2),
            Label(x, BOTTOM + 22, f"{float(b):.2f}", 14, SECONDARY, anchor="middle"),
        ]
    for k in k_ticks:
        _, y = map_point(B_MIN, k)
        scene += [
            line(LEFT, y, RIGHT, y, GRID, 0.75),
            line(LEFT - 5, y, LEFT, y, SECONDARY, 1.2),
            Label(LEFT - 11, y + 5, f"{float(k):.2f}", 14, SECONDARY, anchor="end"),
        ]

    central_dash = (7.0, 4.0)
    product_dash = (1.2, 4.3)
    scene += [
        trace(((A, SHORT_INSERTION), (A, LONG_INSERTION)), GUIDE, 1.1, (3.0, 4.0)),
        trace(((B_MIN, LONG_INSERTION), (LARGE_ERASURE, LONG_INSERTION)), BOUND, 2.0),
        trace(((LARGE_ERASURE, SHORT_INSERTION), (LARGE_ERASURE, LONG_INSERTION)), BOUND, 2.0),
        trace(((A, SHORT_INSERTION), (LARGE_ERASURE, SHORT_INSERTION)), BOUND, 2.0),
        trace(((CENTRAL_SHORT_START, K_MIN),
               (CENTRAL_SHORT_START, central_short(CENTRAL_SHORT_START)),
               (A, central_short(A)), (A, SHORT_INSERTION)), BOUND, 2.0, central_dash),
        trace(((CENTRAL_LONG_START, LONG_INSERTION),
               (CENTRAL_LONG_START, central_long(CENTRAL_LONG_START)),
               (CENTRAL_LONG_JOIN, LONG_INSERTION)), BOUND, 2.0, central_dash),
        trace(((PRODUCT_START, fixed_product(PRODUCT_START)), (A, fixed_product(A))),
              ACCENT, 2.3, product_dash),
        rectangle(LEFT, TOP, RIGHT - LEFT, BOTTOM - TOP, stroke=SECONDARY, line_width=1.35),
        Label(396, 132, "Long insertion  k >= 1089/1420", 17, INK, bold=True, anchor="middle"),
        Label(639, 240, "Large erasure", 17, INK, bold=True, anchor="middle"),
        Label(639, 262, "b >= 1355/1482", 15, INK, anchor="middle"),
        Label(419, 371, "Short insertion", 16, INK, bold=True, anchor="middle"),
        Label(419, 392, "k <= 921/1652 for b >= 3/4", 14, INK, anchor="middle"),
        Label(396, 244, "Open in this map", 21, INK, bold=True, anchor="middle"),
        Label(396, 269, "Other label or divisor selectors can reach target", 13,
              SECONDARY, anchor="middle"),
        Label(21, (TOP + BOTTOM) / 2, "Insertion exponent  k = log_D K",
              17, INK, anchor="middle", angle=-90),
        Label((LEFT + RIGHT) / 2, 469, "Erased cutoff exponent  b = log_D B",
              17, INK, anchor="middle"),
        rectangle(LEFT, 493, 24, 13, FILL, BOUND, 1.2),
        Label(LEFT + 34, 505, "Target O(D^(3/4+eps))", 14),
        line(361, 499, 392, 499, BOUND, 2.0, central_dash),
        Label(403, 505, "Central affine refinements", 14),
        line(LEFT, 528, LEFT + 24, 528, ACCENT, 2.3, product_dash),
        Label(LEFT + 34, 533, "Dotted boundary: fixed label product bounded (xi = 0)", 14),
    ]
    return scene


def fmt(value: float) -> str:
    return f"{value:.5f}".rstrip("0").rstrip(".") or "0"


def svg(scene: list[Shape | Label]) -> bytes:
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" '
        f'viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title description">',
        f'  <title id="title">{escape(TITLE)}</title>',
        f'  <desc id="description">{escape(DESCRIPTION)}</desc>',
        '  <g font-family="Arial, Helvetica, sans-serif" stroke-linecap="round" stroke-linejoin="round">',
    ]
    for item in scene:
        if isinstance(item, Shape):
            commands = [f"{'M' if index == 0 else 'L'}{fmt(x)} {fmt(y)}"
                        for index, (x, y) in enumerate(item.points)]
            if item.closed:
                commands.append("Z")
            stroke = ""
            if item.stroke:
                stroke = f' stroke="{item.stroke}" stroke-width="{fmt(item.width)}"'
                if item.dash:
                    stroke += ' stroke-dasharray="' + " ".join(map(fmt, item.dash)) + '"'
            lines.append(f'    <path d="{" ".join(commands)}" fill="{item.fill or "none"}"{stroke}/>')
        else:
            rotation = (
                f' transform="rotate({fmt(item.angle)} {fmt(item.x)} {fmt(item.y)})"'
                if item.angle else ""
            )
            lines.append(
                f'    <text x="{fmt(item.x)}" y="{fmt(item.y)}" font-size="{fmt(item.size)}" '
                f'fill="{item.color}" text-anchor="{item.anchor}" '
                f'font-weight="{"700" if item.bold else "400"}"{rotation}>'
                f'{escape(item.value)}</text>'
            )
    lines.extend(("  </g>", "</svg>", ""))
    return "\n".join(lines).encode()


def rgb(hex_color: str) -> str:
    return " ".join(fmt(int(hex_color[index:index+2], 16) / 255) for index in (1, 3, 5))


# Standard Helvetica widths in thousandths of an em for the figure's printable ASCII.
_REGULAR = (
    278, 278, 355, 556, 556, 889, 667, 191, 333, 333, 389, 584, 278, 333, 278, 278,
    556, 556, 556, 556, 556, 556, 556, 556, 556, 556, 278, 278, 584, 584, 584, 556,
    1015, 667, 667, 722, 722, 667, 611, 778, 722, 278, 500, 667, 556, 833, 722, 778,
    667, 778, 722, 667, 611, 722, 667, 944, 667, 667, 611, 278, 278, 278, 469, 556,
    333, 556, 556, 500, 556, 556, 278, 556, 556, 222, 222, 500, 222, 833, 556, 556,
    556, 556, 333, 500, 278, 556, 500, 722, 500, 500, 500, 334, 260, 334, 584,
)
_BOLD = (
    278, 333, 474, 556, 556, 889, 722, 238, 333, 333, 389, 584, 278, 333, 278, 278,
    556, 556, 556, 556, 556, 556, 556, 556, 556, 556, 333, 333, 584, 584, 584, 611,
    975, 722, 722, 722, 722, 667, 611, 778, 722, 278, 556, 722, 611, 833, 722, 778,
    667, 778, 722, 667, 611, 722, 667, 944, 667, 667, 611, 333, 278, 333, 584, 556,
    333, 556, 611, 556, 611, 556, 333, 611, 611, 278, 278, 556, 278, 889, 611, 611,
    611, 611, 389, 556, 333, 611, 556, 778, 556, 556, 500, 389, 280, 389, 584,
)


def pdf_string(value: str) -> str:
    return "(" + value.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)") + ")"


def pdf(scene: list[Shape | Label]) -> bytes:
    commands = [f"q 1 0 0 -1 0 {HEIGHT} cm", "1 J 1 j"]
    for item in scene:
        if isinstance(item, Shape):
            if item.fill:
                commands.append(f"{rgb(item.fill)} rg")
            if item.stroke:
                commands.append(f"{rgb(item.stroke)} RG {fmt(item.width)} w")
                commands.append("[" + " ".join(map(fmt, item.dash)) + "] 0 d")
            for index, (x, y) in enumerate(item.points):
                commands.append(f"{fmt(x)} {fmt(y)} {'m' if index == 0 else 'l'}")
            if item.closed:
                commands.append("h")
            commands.append("B" if item.fill and item.stroke else "f" if item.fill else "S")
        else:
            widths = _BOLD if item.bold else _REGULAR
            assert all(32 <= ord(char) <= 126 for char in item.value)
            text_width = item.size * sum(widths[ord(char) - 32] for char in item.value) / 1000
            offset = {"start": 0, "middle": text_width / 2, "end": text_width}[item.anchor]
            theta = radians(item.angle)
            c, s = cos(theta), sin(theta)
            x, y = item.x - offset * c, item.y - offset * s
            text_matrix = " ".join(map(fmt, (c, s, s, -c, x, y)))
            commands.append(
                f"BT /F{'2' if item.bold else '1'} {fmt(item.size)} Tf {rgb(item.color)} rg "
                f"{text_matrix} Tm {pdf_string(item.value)} Tj ET"
            )
    commands.append("Q")
    stream = ("\n".join(commands) + "\n").encode("ascii")
    objects = (
        b"<< /Type /Catalog /Pages 2 0 R /Lang (en) >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        (f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {WIDTH} {HEIGHT}] "
         f"/Resources << /Font << /F1 5 0 R /F2 6 0 R >> >> /Contents 4 0 R >>").encode("ascii"),
        f"<< /Length {len(stream)} >>\nstream\n".encode("ascii") + stream + b"endstream",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>",
        (f"<< /Title {pdf_string(TITLE)} /Subject {pdf_string(DESCRIPTION)} "
         "/Creator (GRH research regime diagram v2) >>").encode("ascii"),
    )
    document = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for number, obj in enumerate(objects, 1):
        offsets.append(len(document))
        document.extend(f"{number} 0 obj\n".encode("ascii") + obj + b"\nendobj\n")
    xref = len(document)
    document.extend(f"xref\n0 {len(offsets)}\n0000000000 65535 f \n".encode("ascii"))
    for offset in offsets[1:]:
        document.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    document.extend(
        f"trailer\n<< /Size {len(offsets)} /Root 1 0 R /Info 7 0 R >>\n"
        f"startxref\n{xref}\n%%EOF\n".encode("ascii")
    )
    return bytes(document)


def checked_source_root(requested: Optional[Path]) -> Path:
    if requested is not None:
        root = requested.resolve(strict=True)
    else:
        root = next((candidate for candidate in (HERE, *HERE.parents)
                     if all((candidate / source).is_file() for source in SOURCES)), None)
        if root is None:
            raise ValueError("Reviewed sources were not found. Supply --source-root.")
    if not root.is_dir():
        raise ValueError(f"Source root is not a directory: {root}")
    for source, digest in SOURCES.items():
        path = root / source
        if not path.is_file() or sha256(path.read_bytes()).hexdigest() != digest:
            raise ValueError(f"Reviewed input is missing or has changed: {source}")
    return root


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path,
                        help="repository directory containing the pinned proofs and review")
    parser.add_argument("--output-dir", type=Path, default=HERE,
                        help="existing directory for new assets; existing files are refused")
    args = parser.parse_args()
    checked_source_root(args.source_root)
    output_dir = args.output_dir.resolve(strict=True)
    if not output_dir.is_dir():
        raise ValueError(f"Output path is not a directory: {output_dir}")
    assert central_long(CENTRAL_LONG_JOIN) == LONG_INSERTION
    assert CENTRAL_LONG_START < CENTRAL_LONG_JOIN < A
    assert central_short(A) == F(25, 44)
    assert fixed_product(A) == F(63, 100)
    scene = make_scene()
    assets = {
        "paired-cutoff-regimes.svg": svg(scene),
        "paired-cutoff-regimes.pdf": pdf(scene),
    }
    manifest = {
        "scope": DESCRIPTION,
        "sources": SOURCES,
        "window": {"b": [str(B_MIN), str(B_MAX)], "k": [str(K_MIN), str(K_MAX)]},
        "broad": {
            "long_insertion_k_min": str(LONG_INSERTION),
            "large_erasure_b_min": str(LARGE_ERASURE),
            "short_insertion_k_max": str(SHORT_INSERTION),
            "short_insertion_b_min": str(A),
        },
        "central_short": {"b_min": str(CENTRAL_SHORT_START), "b_max": str(A),
                          "k_max": "(172b+21)/264"},
        "central_long": {"b_min": str(CENTRAL_LONG_START), "b_max": str(A),
                         "k_min": "(508b+1743)/2768",
                         "displayed_boundary_joins_broad_at_b": str(CENTRAL_LONG_JOIN)},
        "conditional": {"b_min": str(PRODUCT_START), "b_max": str(A),
                        "k_max_at_xi_zero": "(308b+21)/400", "filled": False},
        "assets": {name: {"sha256": sha256(data).hexdigest(), "bytes": len(data)}
                   for name, data in assets.items()},
    }
    assets["regime-data-v2.json"] = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode()
    for name in assets:
        path = output_dir / name
        if path.exists() or path.is_symlink():
            raise FileExistsError(f"Refusing to overwrite {path}")
    for name, data in assets.items():
        with (output_dir / name).open("xb") as handle:
            handle.write(data)


if __name__ == "__main__":
    main()
