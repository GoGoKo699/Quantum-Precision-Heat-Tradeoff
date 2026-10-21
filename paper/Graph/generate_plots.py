#!/usr/bin/env python3
"""Generate the manuscript's quantitative plot directly from its formula.

Run from any directory: python /path/to/Graph/generate_plots.py
The default output is Graph/crossover.pdf, beside this script. No input dataset,
TeX engine or repository import is needed. The Bloch-circle and apparatus diagrams
are TikZ code in Quantum_Precision_Heat_Tradeoff_arXiv.tex, not external graphics.

The plot is the joint limiting law for each finite r, not a finite-device optimum
or experimental data. Its stable evaluation matches qph.core.crossover; tests in
the repository compare the portable implementation against the canonical one.
"""
from __future__ import annotations

import argparse
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, LogFormatterMathtext, FormatStrFormatter

LN2 = math.log(2.0)
CM = 1.0 / 2.54


def binary_deficit(b: float) -> float:
    """Return 1-h2((1+b)/2), stably for b near zero or one."""
    b = float(b)
    if not math.isfinite(b) or not 0.0 <= b <= 1.0:
        raise ValueError("Bias must be finite and in [0,1].")
    if b == 1.0:
        return 1.0
    if b < 0.01:
        square = b * b
        return square * math.fsum(
            square**k / ((2*k+2)*(2*k+1)) for k in range(6)
        ) / LN2
    return ((1+b)*math.log1p(b)+(1-b)*math.log1p(-b))/(2*LN2)


def crossover(r: float) -> float:
    """The optimal joint-limit heat F(r), in units of k_B T ln(2)."""
    r = float(r)
    if not math.isfinite(r) or r < 0.0:
        raise ValueError("The limiting ratio must be finite and nonnegative.")
    return binary_deficit(0.5/math.sqrt(r+0.25))


def sample_curve(count: int = 901) -> tuple[list[float], list[float]]:
    """Sample the displayed finite positive ratios 10^-3 through 10^2."""
    if not isinstance(count, int) or isinstance(count, bool) or count < 2:
        raise ValueError("At least two samples are required.")
    r = [10.0**(-3.0+5.0*i/(count-1)) for i in range(count)]
    return r, [crossover(x) for x in r]


def draw(output: Path) -> None:
    """Write a vector PDF; all content is produced by Matplotlib."""
    r, heat = sample_curve()
    # Preserve the approved manuscript colors, typography and panel geometry.
    settings = {
        "font.family": "serif", "font.serif": ["cmr10"],
        "font.size": 9, "mathtext.fontset": "cm", "axes.formatter.use_mathtext": True,
        "pdf.fonttype": 42, "ps.fonttype": 42,
        "axes.linewidth": 0.5, "xtick.major.width": 0.4, "ytick.major.width": 0.4,
        "xtick.major.size": 2.3, "ytick.major.size": 2.3,
        "axes.unicode_minus": False,
    }
    with plt.rc_context(settings):
        fig = plt.figure(figsize=(8.5*CM, 6.4*CM))
        ax = fig.add_axes([1.6/8.5, 1.5/6.4, 5.9/8.5, 3.75/6.4])
        ax.set_xscale("log")
        ax.set_xlim(1e-3, 1e2)
        ax.set_ylim(0, 1.04)
        ax.set_xlabel(r"$r=\lim\,\epsilon/s^2$", labelpad=6)
        ax.set_ylabel(r"$F(r)$ in units of $k_{\mathrm{B}}T\ln 2$", labelpad=5)
        ax.xaxis.set_major_locator(LogLocator(base=10, numticks=6))
        ax.xaxis.set_major_formatter(LogFormatterMathtext())
        ax.set_yticks([0, .2, .4, .6, .8, 1])
        ax.yaxis.set_major_formatter(FormatStrFormatter("%g"))
        ax.tick_params(labelsize=8)
        ax.minorticks_off()
        ax.grid(which="major", color="0.9", linewidth=.45)
        ax.spines[["right", "top"]].set_visible(False)
        ax.plot(r, heat, color="#184a6e", linewidth=1.1)
        f1 = crossover(1.0)
        ax.plot([1.0], [f1], "o", color="#184a6e", markersize=3.8, zorder=4)
        ax.text(2.15, .28, r"$r=1$"+"\n"+r"$F\simeq0.149510$",
                ha="left", va="center", fontsize=8)
        ax.plot([1.83, 1], [.245, f1], color="0.45", linewidth=.5)
        ax.text(.025, 1.10, r"$F(0)=1$ (endpoint)", transform=ax.transAxes,
                ha="left", va="bottom", fontsize=8)
        # PDF metadata dates are omitted so the generated asset is reproducible.
        output.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output, format="pdf", metadata={
            "Title": "Optimal limiting precision-heat crossover",
            "Author": "Ranyiliu Chen; Ruge Lin",
            "Subject": "Analytic joint limiting law; not finite optima or experimental data",
            "Creator": "Graph/generate_plots.py (Matplotlib)",
            "CreationDate": None, "ModDate": None,
        })
        plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().with_name("crossover.pdf"))
    args = parser.parse_args()
    draw(args.output)
    print(f"Wrote {args.output}; F(0)={crossover(0):.15g}, F(1)={crossover(1):.15g}")


if __name__ == "__main__":
    main()
