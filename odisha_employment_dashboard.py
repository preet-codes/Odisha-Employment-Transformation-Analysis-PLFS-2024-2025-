import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------
# Basic page setup
# ---------------------------
st.set_page_config(page_title="Odisha Employment Story", layout="wide")

# ---------------------------
# Styling (simple glass feel)
# ---------------------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #020617, #0f172a);
}

section.main > div {
    background: rgba(255,255,255,0.04);
    padding: 25px;
    border-radius: 18px;
    backdrop-filter: blur(10px);
}

h1, h2, h3 {
    color: #e2e8f0;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Title
# ---------------------------
st.title("📊 Odisha Employment Transformation")
st.markdown("### PLFS 2024–2025 Analysis")

# ---------------------------
# Load data
# ---------------------------
# Using cache so file is not reloaded every time
@st.cache_data
def load_data():
    return pd.read_csv("/data/PLFS_ODISHA_FINAL.csv")

df = load_data()

# ---------------------------
# Basic cleaning
# ---------------------------

# Remove duplicate columns if any (sometimes happens after merge)
df = df.loc[:, ~df.columns.duplicated()]

# Convert important fields to numeric
df['year'] = pd.to_numeric(df['year'], errors='coerce')
df['weight'] = pd.to_numeric(df['weight'], errors='coerce')

# Convert codes to readable labels
df['sector'] = df['sector'].map({1: 'Rural', 2: 'Urban'}).fillna('Unknown')
df['gender'] = df['gender'].map({1: 'Male', 2: 'Female'}).fillna('Other')

# Clean sector names
df['employment_sector'] = df['employment_sector'].str.strip().str.title()

# Create a simpler classification for hypothesis
df['broad_sector'] = df['employment_sector'].apply(
    lambda x: 'Agriculture' if x == 'Agriculture' else 'Non-Agriculture'
)

# Drop bad rows
df = df.dropna(subset=['year', 'weight', 'employment_sector'])

# ---------------------------
# Sidebar filters
# ---------------------------
st.sidebar.header("Filters")

selected_gender = st.sidebar.multiselect(
    "Gender",
    df['gender'].unique(),
    default=df['gender'].unique()
)

selected_area = st.sidebar.multiselect(
    "Area",
    df['sector'].unique(),
    default=df['sector'].unique()
)

# Apply filters
df = df[
    (df['gender'].isin(selected_gender)) &
    (df['sector'].isin(selected_area))
]

# ---------------------------
# SECTION 1 — Key Metrics
# ---------------------------
st.markdown("## 🧠 What changed?")

# Weighted distribution
dist = df.pivot_table(
    index='year',
    columns='broad_sector',
    values='weight',
    aggfunc='sum'
)

# Convert to proportions
dist = dist.div(dist.sum(axis=1), axis=0)

# Extract values
agri_2024 = dist.loc[2024, 'Agriculture']
agri_2025 = dist.loc[2025, 'Agriculture']
change = agri_2025 - agri_2024

# Show metrics
c1, c2, c3 = st.columns(3)
c1.metric("Agriculture 2024", f"{agri_2024:.2%}")
c2.metric("Agriculture 2025", f"{agri_2025:.2%}")
c3.metric("Change", f"{change:.2%}")

# Simple interpretation
if change < 0:
    st.success(f"Agriculture share declined by {abs(change):.2%}")
else:
    st.warning("No clear decline in agriculture share")

# ---------------------------
# SECTION 2 — Sector Breakdown
# ---------------------------
st.markdown("## 📊 Sector composition")

sector_dist = (
    df.groupby(['year', 'employment_sector'], as_index=False)['weight']
    .sum()
)

# Normalize within each year
sector_dist['weight'] = sector_dist.groupby('year')['weight'].transform(
    lambda x: x / x.sum()
)

fig1 = px.bar(
    sector_dist,
    x='year',
    y='weight',
    color='employment_sector',
    barmode='stack'
)

fig1.update_layout(template='plotly_dark', xaxis_type='category')
st.plotly_chart(fig1, use_container_width=True)

# ---------------------------
# SECTION 3 — Trend
# ---------------------------
st.markdown("## 📈 Agriculture vs Non-Agriculture")

trend = (
    df.groupby(['year', 'broad_sector'], as_index=False)['weight']
    .sum()
)

trend['weight'] = trend.groupby('year')['weight'].transform(
    lambda x: x / x.sum()
)

fig2 = px.line(
    trend,
    x='year',
    y='weight',
    color='broad_sector',
    markers=True
)

fig2.update_layout(template='plotly_dark', xaxis_type='category')
st.plotly_chart(fig2, use_container_width=True)

# ---------------------------
# SECTION 4 — Gender
# ---------------------------
st.markdown("## 👥 Gender distribution")

gender = (
    df.groupby(['gender', 'employment_sector'], as_index=False)['weight']
    .sum()
)

gender['weight'] = gender.groupby('gender')['weight'].transform(
    lambda x: x / x.sum()
)

fig3 = px.bar(
    gender,
    x='gender',
    y='weight',
    color='employment_sector',
    barmode='stack'
)

fig3.update_layout(template='plotly_dark')
st.plotly_chart(fig3, use_container_width=True)

# ---------------------------
# SECTION 5 — Rural vs Urban
# ---------------------------
st.markdown("## 🏙️ Rural vs Urban")

ru = (
    df.groupby(['sector', 'employment_sector'], as_index=False)['weight']
    .sum()
)

ru['weight'] = ru.groupby('sector')['weight'].transform(
    lambda x: x / x.sum()
)

fig4 = px.bar(
    ru,
    x='sector',
    y='weight',
    color='employment_sector',
    barmode='stack'
)

fig4.update_layout(template='plotly_dark')
st.plotly_chart(fig4, use_container_width=True)

# ---------------------------
# Final summary
# ---------------------------
st.markdown("## 🎯 Summary")

st.write(f"""
Agriculture share moved from {agri_2024:.2%} to {agri_2025:.2%}.

Overall change: {change:.2%}

This suggests a gradual shift towards non-agriculture sectors,
though the pace of change is still moderate.
""")