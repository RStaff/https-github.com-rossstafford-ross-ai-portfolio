# Ross AI Portfolio
# Analytics & Data-Quality Mini-Portfolio

**Author**: Ross Stafford • PMP® | Data & Product PM  
**Live repo**: <https://github.com/RStaff/https-github.com-rossstafford-ross-ai-portfolio>

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![CI](https://img.shields.io/github/actions/workflow/status/RStaff/https-github.com-rossstafford-ross-ai-portfolio/ci.yml?label=CI%2FCD)

---

## 📈 Project 1 — GA4 Foot-Traffic Forecast MVP
A small experiment built in 2024 to see if store-visit data can predict sales (“alpha” = trading signal).
I merged Google Analytics 4 visit counts (people near each store) with that store’s point-of-sale revenue for the same weeks. 
I used PySpark to engineer and store model features (e.g., 7-day lag, rolling averages) in a scalable way. 
I trained Random-Forest model, the machine-learning algorithm you trained to predict next week’s sales. 
The model’s average error was 8 % lower than a very simple benchmark (e.g., “next week = this week”). 
In other words, it’s meaningfully more accurate. The predictions identified stores whose sales were likely to significantly beat or miss expectations; statistical test shows only a 3 % chance the signal is random (good).

| Step | Tech | Outcome |
|------|------|---------|
| ETL  | **Python / pandas** | Join synthetic GA4 geofence events with POS sales |
| Model| **scikit-learn RandomForest** | ↓ MAE 8 % vs. naïve baseline |
| Viz  | **Looker Studio** | Dual-axis chart for planners (sales vs. visits) |

![Looker screenshot](ga4_dashboard/chart.png)

### Reproduce locally

```bash
cd ga4_dashboard
python3 foot_traffic.ipynb  # or open in JupyterLab
open chart.png              # exported Looker chart

**🛡️ Project 2 — Airflow Data-Quality Guard Rails**
Check	Logic	Alert
Row count	Fail if < 700 rows	Airflow task → red
Null ratio	Fail if any visits NULLs	Upstream-failed

🏗️ Architecture
          GA4 events           POS csv
                │                 │
                └───► pandas — RandomForest —► predictions.csv
                                         │
  Looker Studio dashboard ◄──────────────┘
                                         ▼
           Airflow (row & null checks) — SQLite


🔍 Tech Stack
Python 3.11, pandas, scikit-learn

Docker Compose (Airflow 2.9, Postgres, Redis)

Looker Studio • SQLite • GitHub Actions (CI / Trivy / Bandit)

📝 License
MIT — free to fork & remix. Attribution appreciated!

