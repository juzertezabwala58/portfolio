# 📊 Power BI & Business Intelligence Portfolio

This directory contains interactive Microsoft Power BI dashboards, data models, DAX measures, automated JSON theme generators, and retail/sports analytical projects.

---

## 📂 Projects & Dashboards

### 1. [IPL Cricket Analytics Dashboard & Theme Suite](./01_ipl_cricket_analytics/)
- **Description**: Multi-page executive cricket analytics dashboard covering match overviews, batter strike rates across phases (Powerplay, Middle, Death), and bowler economies.
- **Includes**: `ipl_dashboard_data.pbix`, Python Base64 Theme Generator (`theme_converter.py`), custom theme (`cricket_theme.json`), and dashboard mockups.

### 2. [Supermarket Retail Sales Analytics](./02_supermarket_sales_analytics/)
- **Description**: Executive retail business dashboard analyzing gross revenue, profit margins, branch benchmarks, product categories, and customer payment methods.
- **Includes**: `supermarket_sales_analysis.pbix`, `supermarket_sales_data.csv`.

### 3. [Player Performance & Sports Analytics](./03_player_performance_analytics/)
- **Description**: In-depth player scoring, match-impact indexing, milestone tracking, and head-to-head opposition performance analytics.
- **Includes**: `player_stats.pbix`.

---

## ⚡ Quick Start
- To view any dashboard, open the respective `.pbix` file in **Microsoft Power BI Desktop**.
- To generate custom Power BI JSON themes with embedded backgrounds, run `python 01_ipl_cricket_analytics/theme_converter.py`.
