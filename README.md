# FoodHub Data Analysis

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/actiomlabs-eng/Foodhub_Data_Analysis/blob/main/notebooks/foodhub_data_analysis.ipynb)

Exploratory data analysis of an NYC food-delivery aggregator's order dataset, using Python (pandas, NumPy, Matplotlib, Seaborn) to surface restaurant demand patterns, cuisine popularity, delivery-time behavior, and revenue insights.

> **Source acknowledgment:** Project framing, dataset, and analytical questions are from the **UT Austin ML and AI** coursework ("Project Python Foundations: FoodHub Data Analysis"). All code, analysis, and observations in this repository are my own work.

---

## Problem context

The number of restaurants in New York is increasing rapidly, and students and busy professionals rely heavily on food-delivery apps. **FoodHub** is a fictional aggregator offering access to multiple restaurants through a single smartphone app. The company earns revenue by charging restaurants a fixed margin on each delivered order.

## Objective

The company's data science team wants to analyze stored order data to better understand demand across restaurants and cuisines, characterize delivery and prep-time performance, and surface insights that can improve customer experience and revenue. This notebook answers **17 business-driven questions** posed by the team, spanning data quality, univariate distributions, multivariate relationships, and revenue/operations metrics.

## Dataset

- **File:** `data/raw/foodhub_order.csv` (~124 KB, committed to the repo)
- **Grain:** one row per customer order

### Data dictionary

| Column | Description |
|---|---|
| `order_id` | Unique ID of the order |
| `customer_id` | ID of the customer who placed the order |
| `restaurant_name` | Name of the restaurant |
| `cuisine_type` | Cuisine ordered |
| `cost_of_the_order` | Order cost (USD) |
| `day_of_the_week` | `Weekday` (Mon–Fri) or `Weekend` (Sat–Sun) |
| `rating` | Customer rating out of 5 (or `Not given`) |
| `food_preparation_time` | Minutes between restaurant order confirmation and pickup |
| `delivery_time` | Minutes between pickup and drop-off |

## Methodology

1. **Data quality** — shape, dtypes, missing values, statistical summary
2. **Univariate EDA** — distributions of cost, delivery time, prep time, cuisine, day of week, rating
3. **Multivariate EDA** — relationships between cuisine, rating, day of week, total time
4. **Business questions** — top-N restaurants, weekend cuisine demand, revenue under company commission rules, on-time delivery rates, weekday vs. weekend delivery patterns
5. **Conclusions & recommendations** — synthesized findings for the imagined product team

## Key results

**Headline findings** (computed from 1,898 orders across 14 cuisine types):

- **71%** of orders placed on weekends; **American** cuisine leads with **30.7%** share
- **38.8%** of orders went unrated — the largest data-quality gap and a clear product opportunity (rating prompts, incentives)
- Top 5 restaurants by volume: **Shake Shack** (219), **The Meatball Shop** (132), **Blue Ribbon Sushi** (119), **Blue Ribbon Fried Chicken** (96), **Parm** (68)
- Net revenue under tiered commission rules (25% on orders >$20, 15% on $5–20): **~$6,166** across the dataset
- **10.5%** of orders exceed 60 min total fulfillment time — an SLA-breach segment worth targeted ops follow-up
- Weekday delivery is **~6 minutes slower** than weekend delivery — a routing/staffing signal

For full visualizations (univariate distributions, multivariate relationships, cuisine-by-rating patterns), see the executed [notebook](notebooks/foodhub_data_analysis.ipynb) — plots render inline on GitHub.

## Tech stack

- **Python** 3.11
- **pandas**, **NumPy** — data manipulation
- **Matplotlib**, **Seaborn** — visualization
- **Jupyter Lab** — notebook environment

Pinned versions in [`requirements.txt`](requirements.txt).

## How to run

```bash
# 1. Clone
git clone https://github.com/actiomlabs-eng/Foodhub_Data_Analysis.git
cd Foodhub_Data_Analysis

# 2. Create + activate a virtual environment (Python 3.11)
python3.11 -m venv .venv
source .venv/bin/activate          # macOS / Linux
# .venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the notebook
jupyter lab notebooks/foodhub_data_analysis.ipynb
```

The dataset is committed at `data/raw/foodhub_order.csv` — no download step required.

## Repository structure

```
Foodhub_Data_Analysis/
├── notebooks/
│   └── foodhub_data_analysis.ipynb     # cleaned analysis notebook
├── src/
│   └── eda.py                          # extracted reusable EDA helpers
├── data/
│   └── raw/
│       └── foodhub_order.csv           # source dataset (tracked)
├── tests/                              # pytest for src/ helpers
├── requirements.txt
├── README.md
└── LICENSE
```

## License

[MIT](LICENSE) — for the code in this repository. The dataset and original problem framing are credited to **UT Austin ML and AI**.
