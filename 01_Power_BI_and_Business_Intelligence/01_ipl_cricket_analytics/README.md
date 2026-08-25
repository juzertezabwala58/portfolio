# 🏏 IPL Cricket Analytics Dashboard & Power BI Theme Suite

## 📌 Project Overview
An interactive, multi-view Power BI dashboard suite providing comprehensive analytics on Indian Premier League (IPL) matches, player metrics, batting strike rates, bowling economies, and team performance trends. Includes an automated Python utility to convert custom canvas backgrounds into compliant Power BI JSON theme schemas.

---

## 📊 Dashboard Views & Pages

### 1. **Executive Match Overview Dashboard** (`overview_dashboard.png`)
- **Key KPIs**: Total Matches Played, Total Runs Scored, Total Wickets Taken, Boundary Percentages (4s & 6s).
- **Match Trends**: Season-by-season progression, toss decision vs match win probability, venue analytics.

### 2. **Batter's Performance Analytics** (`batters_dashboard.png`)
- **Player Stats**: Individual strike rates, boundary distribution, performance against pace vs spin.
- **Phase Breakdown**: Powerplay (Overs 1-6), Middle Overs (7-15), and Death Overs (16-20) run rates.

### 3. **Bowler's Performance Analytics** (`bowlers_dashboard.png`)
- **Economy & Wicket Ratios**: Dot-ball percentage, economy rates across innings phases, bowling average.

---

## 🛠️ Components & Files
- `ipl_dashboard_data.pbix`: Full interactive Microsoft Power BI Report File.
- `overview_dashboard.png`: Executive dashboard design mockup.
- `batters_dashboard.png`: Batter performance analytics page.
- `bowlers_dashboard.png`: Bowler performance analytics page.
- `template.png` & `background.png`: Custom canvas layouts and UI backgrounds.
- `theme_converter.py`: Automated Base64 image-to-JSON Power BI theme generator.
- `cricket_theme.json`: Official Power BI Theme JSON file.

---

## ⚡ How to Open or Generate
1. **Open Report**: Open `ipl_dashboard_data.pbix` in Power BI Desktop.
2. **Generate Custom Theme**:
   ```bash
   python theme_converter.py
   ```
