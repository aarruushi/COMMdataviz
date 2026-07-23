"""
Most Successful US Robotics Companies (2025) — matplotlib chart.

Reads robotics_companies_us_2025.csv and renders a horizontal bar chart
ranking companies by valuation / market cap. Saves PNGs in light and dark.

Usage:
    python robotics_chart.py

Requires: matplotlib, pandas
    pip install matplotlib pandas
"""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

HERE = Path(__file__).parent
CSV = HERE / "robotics_companies_us_2025.csv"

# Palette (from the data-viz reference palette)
LIGHT = {
    "surface": "#fcfcfb", "ink": "#0b0b0b", "ink2": "#52514e",
    "muted": "#898781", "grid": "#e1e0d9", "bar": "#2a78d6",
}
DARK = {
    "surface": "#1a1a19", "ink": "#ffffff", "ink2": "#c3c2b7",
    "muted": "#898781", "grid": "#2c2c2a", "bar": "#3987e5",
}


def fmt_b(v):
    """Format a USD-billions value like $180B or $2.6B."""
    return f"${v:.0f}B" if v >= 10 else f"${v:.1f}B"


def render(df, theme, out_path):
    c = theme
    # Sort ascending so the largest bar sits at the top of a horizontal chart.
    d = df.sort_values("Valuation_or_MarketCap_USD_B", ascending=True)
    names = d["Company"]
    vals = d["Valuation_or_MarketCap_USD_B"]

    fig, ax = plt.subplots(figsize=(9, 7.5), dpi=150)
    fig.patch.set_facecolor(c["surface"])
    ax.set_facecolor(c["surface"])

    y = range(len(d))
    ax.barh(list(y), vals, height=0.66, color=c["bar"], zorder=3)

    # Direct value labels so small bars stay legible despite the huge top value.
    xmax = vals.max()
    for yi, v in zip(y, vals):
        ax.text(v + xmax * 0.008, yi, fmt_b(v), va="center", ha="left",
                fontsize=9, color=c["ink2"], zorder=4)

    ax.set_yticks(list(y))
    ax.set_yticklabels(names, fontsize=10, color=c["ink2"])
    ax.set_xlim(0, xmax * 1.12)
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"${x:.0f}B"))
    ax.tick_params(axis="x", colors=c["muted"], labelsize=9)
    ax.tick_params(axis="y", length=0)

    # Recessive chrome: light vertical grid, no box.
    ax.grid(axis="x", color=c["grid"], linewidth=1, zorder=0)
    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.set_title("Most Successful US Robotics Companies",
                 fontsize=16, fontweight="bold", color=c["ink"],
                 loc="left", pad=34)
    ax.text(0, 1.015, "Ranked by valuation or market cap, USD billions · 2025",
            transform=ax.transAxes, fontsize=10.5, color=c["ink2"],
            va="bottom", ha="left")

    fig.text(0.01, 0.01,
             "Figures are approximate and illustrative — verify against primary "
             "sources before use.",
             fontsize=7.5, color=c["muted"], ha="left", va="bottom")

    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(out_path, facecolor=c["surface"])
    plt.close(fig)
    print(f"wrote {out_path}")


def main():
    df = pd.read_csv(CSV)
    render(df, LIGHT, HERE / "robotics_chart.png")
    render(df, DARK, HERE / "robotics_chart_dark.png")


if __name__ == "__main__":
    main()
