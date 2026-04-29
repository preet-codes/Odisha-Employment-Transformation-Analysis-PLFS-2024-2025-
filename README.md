# 📊 Odisha Employment Transformation Analysis (PLFS 2024–2025)

## 🚀 Project Overview

This project analyzes structural changes in employment patterns in Odisha using **PLFS (Periodic Labour Force Survey) 2024–2025** unit-level data.

The primary goal is to test the hypothesis:

> **Is Odisha experiencing a shift from Agriculture to Non-Agriculture employment?**

To answer this, we combine:

* Statistical analysis (Chi-square test)
* Weighted survey data processing
* Interactive data storytelling dashboard (Streamlit)

---

## 🧠 Key Objectives

* Identify sector-wise employment distribution
* Detect structural shifts in workforce composition
* Validate findings using statistical hypothesis testing
* Build an intuitive dashboard for stakeholders

---

## 📂 Data Sources

### 1. PLFS 2024

* `CHHV1.csv` → Household data
* `CPERV1.csv` → Person-level data

### 2. PLFS 2025

* `CHHV1.TXT`
* `CPERV1.TXT`
* Layout file: `Data_LayoutPLFS_2025.xlsx`

---

## ⚙️ Data Processing Pipeline

### Step 1 — Data Cleaning

* Standardized column names (lowercase)
* Converted relevant columns to numeric
* Removed null and inconsistent records

---

### Step 2 — Merging Data

Merged household and person-level data using:

```
['sector','state','district','fsu','sss','hh_id']
```

This ensures each individual is enriched with household-level attributes.

---

### Step 3 — Filtering Workforce

We focus on **actively employed individuals**:

| Code | Meaning          |
| ---- | ---------------- |
| 11   | Self-employed    |
| 12   | Regular salaried |
| 21   | Casual labour    |

This removes unemployed / inactive population for accurate analysis.

---

### Step 4 — Applying Weights

PLFS is survey data, not full population data.

We compute:

```
weight = multiplier / 100
```

This ensures results reflect **true population estimates**.

---

### Step 5 — Sector Classification

Industries (NIC codes) are grouped:

* 01–03 → Agriculture 🌾
* 05–39 → Manufacturing 🏭
* 45+ → Services 🏢
* Others → Misc

---

### Step 6 — Combine Years

```
df_all = pd.concat([df_2024, df_2025])
```

Adds:

```
year = 2024 / 2025
```

---

## 📊 Hypothesis Testing

### Hypothesis

* **H0:** No structural shift
* **H1:** Structural shift exists

### Method

Chi-square test on weighted contingency table:

```
broad_sector vs year
```

### Result

```
p-value: ~0.0
```

👉 Reject H0
👉 **Statistically significant shift observed**

---

## 📈 Key Findings

* Agriculture share declined (~3–4%)
* Non-agriculture sectors increased
* Services sector is the primary driver
* Shift varies across gender and rural/urban areas

---

## 🖥️ Dashboard Features

Built using **Streamlit + Plotly**

### Sections:

1. 🧠 What Changed (KPIs)
2. 📊 Sector Composition
3. 📈 Trend Analysis
4. 👥 Gender Insights
5. 🏙️ Rural vs Urban
6. 🎯 Final Narrative

---

## 🎯 Example Insights

* Agriculture → Declining trend
* Services → Growing sector
* Rural areas → Still agriculture-heavy
* Urban areas → More diversified employment

---

## 🛠️ Tech Stack

* Python (Pandas, NumPy)
* SciPy (Chi-square test)
* Plotly (visualization)
* Streamlit (dashboard)

---

## 📦 Output

Final dataset:

```
PLFS_ODISHA_FINAL.csv
```

Dashboard:

```
Streamlit App
```

---

## 🚀 How to Run

### 1. Install dependencies

```
pip install pandas numpy matplotlib scipy plotly streamlit
```

### 2. Run dashboard

```
streamlit run app.py
```

---

## 📸 Screenshots

(Add your dashboard screenshots here)

---

## 🎤 Interview Explanation (Short Version)

> “I used weighted PLFS survey data to analyze employment shifts in Odisha and validated structural transformation using a Chi-square test. I then built a storytelling dashboard to communicate insights effectively.”

---

## 🔮 Future Improvements

* District-level analysis
* Time-series trend (multi-year)
* Predictive modeling
* Income vs employment linkage

---

## 👤 Author

**Prateek Setia**

---

## ⭐ Final Note

This project demonstrates:

* Data cleaning at scale
* Survey data handling
* Statistical testing
* Data storytelling

---
