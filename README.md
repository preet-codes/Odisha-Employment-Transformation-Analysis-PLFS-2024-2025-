# 📊 Odisha Employment Transformation Analysis (PLFS 2024–2025)

## 🚀 Overview

In this project, I explored how employment patterns in Odisha are changing using PLFS (Periodic Labour Force Survey) data for 2024 and 2025.

The main question I wanted to answer was:

> **Is there a shift happening from Agriculture to Non-Agriculture employment?**

To approach this, I worked with raw survey data, applied weights, performed statistical testing, and finally built a dashboard to visualize the story.

## 🌐 Live Dashboard

You can explore the interactive dashboard here:

🔗 https://odisha-employment-plfs-2024-2025-analysis.streamlit.app/

This dashboard presents a clean, interactive view of employment trends across sectors, gender, and rural-urban segments using PLFS data.

---

## 🧠 What I Tried to Do

* Understand how people are distributed across different sectors
* Check if there is any real structural shift in employment
* Validate that shift using a statistical test (Chi-square)
* Present everything in a simple, visual way using a dashboard

---

## 📂 Data Sources

The data comes from the official PLFS datasets released by the Government of India.
Please download and store the data in /data/PLFS 2025/ and /data/PLFS 2024/ folders respectively.

🔗 **Official Source (MoSPI):**
https://mospi.gov.in

🔗 **PLFS Microdata Download Portal:**
https://microdata.gov.in/nada43/index.php/catalog/PLFS

### Files used:

#### 📅 PLFS 2024

* `CHHV1.csv` → Household-level data
* `CPERV1.csv` → Person-level data

#### 📅 PLFS 2025

* `CHHV1.TXT` → Household data
* `CPERV1.TXT` → Person data
* `FV_Data_LayoutPLFS_2025.xlsx` → Layout file (used to parse TXT data)

⚠️ Note:

* 2024 data is already in CSV format
* 2025 data is in fixed-width TXT format, so it required parsing using layout specifications

---

## ⚙️ How the Data Was Processed

### 1. Cleaning

* Converted all column names to lowercase
* Changed relevant columns to numeric
* Removed invalid or missing values

---

### 2. Merging

Household and person-level datasets were merged using:

```
['sector','state','district','fsu','sss','hh_id']
```

This helps attach household attributes (like income, type, etc.) to each individual.

---

### 3. Filtering the Workforce

I only kept people who are actually working:

| Code | Meaning       |
| ---- | ------------- |
| 11   | Self-employed |
| 12   | Salaried      |
| 21   | Casual labour |

This avoids mixing in unemployed or inactive population.

---

### 4. Applying Weights

Since PLFS is survey data, each record represents multiple people.

So I used:

```
weight = multiplier / 100
```

This ensures results reflect the actual population.

---

### 5. Sector Classification

Industry codes (NIC) were grouped into simpler categories:

* 01–03 → Agriculture
* 05–39 → Manufacturing
* 45+ → Services
* Others → Misc

This makes trends easier to interpret.

---

### 6. Combining Data

Both years were combined into one dataset:

```
df_all = pd.concat([df_2024, df_2025])
```

and a `year` column was added for comparison.

---

## 📊 Hypothesis Testing

### What I tested:

* **H0 (Null):** No change in employment distribution
* **H1:** There is a change

### How:

* Created a **weighted contingency table**
* Applied **Chi-square test**

### Result:

```
p-value ≈ 0
```

👉 This means the change is statistically significant
👉 So we reject the null hypothesis

---

## 📈 Key Observations

* Agriculture share shows a decline (based on weighted proportions)
* Non-agriculture sectors are gaining share
* Services sector is contributing the most to the shift
* Patterns differ across gender and rural/urban areas

---

## 🖥️ Dashboard (Interactive + Live)

I built a Streamlit dashboard to make the analysis easier to explore.

It includes:

* 📌 Key metrics (Agriculture share, change)
* 📊 Sector-wise distribution
* 📈 Trend over time
* 👥 Gender-based breakdown
* 🏙️ Rural vs Urban comparison

---

## 📦 Output

* Final cleaned dataset:

```
PLFS_ODISHA_FINAL.csv
```

* Interactive dashboard:

```
odisha_employment_dashboard.py (Streamlit)
```

---

## 🚀 How to Run

### Install dependencies

```
pip install requirements.txt
```

### Run the dashboard

```
streamlit run odisha_employment_dashboard.py
```

---

## 📸 Dashboard Screenshots:

* Please find the Screenshots and Screen Recording in this folder :
```
Dashboard Screenshots and Recording
``` 

---

Note: Excel parsing dependencies are not included since the final dataset is already processed and provided.


## 👤 Author

**Prateek Setia**

---

