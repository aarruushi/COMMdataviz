# Most Successful Robotics Companies in the US (2025)

A small dataset and starting point for visualizing the leading robotics
companies operating in the United States as of 2025.

## Contents

- **`robotics_companies_us_2025.csv`** — the dataset (15 companies)
- **`README.md`** — this file

## About the dataset

The dataset ranks 15 notable US robotics companies, ordered roughly by
valuation / market capitalization. It spans several robotics segments —
surgical, warehouse, humanoid, drone delivery, agricultural, consumer, and
service robots — to give a cross-section of the industry rather than a single
niche.

### Columns

| Column | Description |
| --- | --- |
| `Company` | Company name |
| `Headquarters` | City of the company's headquarters |
| `State` | US state |
| `Founded` | Year founded |
| `Category` | Primary robotics segment |
| `Ownership` | `Public` or `Private` |
| `Ticker` | Stock ticker (public companies only) |
| `Valuation_or_MarketCap_USD_B` | Market cap (public) or latest private valuation, in billions USD |
| `Est_2024_Revenue_USD_M` | Approximate 2024 revenue, in millions USD |
| `Total_Funding_USD_M` | Total venture funding raised, in millions USD (private companies) |
| `Employees` | Approximate headcount |
| `Flagship_Product` | Best-known product or platform |

### Companies included

Intuitive Surgical, Symbotic, Nuro, Zipline, Figure AI, Skydio, Locus
Robotics, Path Robotics, Boston Dynamics, Agility Robotics, Bright Machines,
Bear Robotics, iRobot, Diligent Robotics, Carbon Robotics.

## Ideas for visualizations

- **Bar chart** — companies by valuation / market cap
- **Bubble chart** — funding raised vs. employees, sized by valuation
- **Grouped bars** — public vs. private companies
- **Map** — headquarters plotted by state (CA and MA dominate)
- **Treemap** — market share by robotics category
- **Scatter** — founding year vs. valuation (how fast newer entrants scaled)

## Important note on the data

These figures are **approximate and illustrative**, compiled for a data-viz
practice project. Valuations, revenue, funding, and headcounts for private
companies in particular change frequently and are not always publicly
disclosed. Blank cells (e.g. `Total_Funding_USD_M` for public companies)
indicate a figure that is not applicable or not readily available. **Verify
against primary sources before using any of these numbers for research,
reporting, or decisions.**
