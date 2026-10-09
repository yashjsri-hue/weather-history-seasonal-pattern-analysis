import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="Weather History Analysis",
    page_icon="🌦️",
    layout="wide"
)

# ---------------- LOAD CLEANED DATA ----------------
df = pd.read_csv("weather_history_cleaned.csv")

# ---------------- CALCULATE KPIs ----------------
total_records = len(df)
avg_temperature = df["Temperature (C)"].mean()
avg_humidity = df["Humidity"].mean() * 100
avg_wind_speed = df["Wind Speed (km/h)"].mean()

# ---------------- NAVIGATION ----------------
sections = [
    "Executive Dashboard",
    "Temperature Analysis",
    "Precipitation Analysis"
]

with st.sidebar:
    st.title("🌦️ Weather Analytics")
    st.caption("Dashboard Navigation")

    selected_section = st.radio(
        "Navigate to",
        sections,
        index=0
    )

# ---------------- PREPARE MONTHLY DATA ----------------
month_names = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

# ---------------- PREPARE YEARLY DATA ----------------
# Exclude 2005 because it has only one record.
year_df = df[df["Year"] >= 2006].copy()

# ---------------- DASHBOARD TITLE ----------------
st.title("🌦️ Weather History & Seasonal Pattern Analysis")

# ====================================================
# PAGE 1: EXECUTIVE DASHBOARD
# ====================================================
if selected_section == "Executive Dashboard":

    st.subheader("Executive Dashboard")
    st.caption("An overview of historical weather patterns")

    # KPI cards in one horizontal row
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Weather Records", f"{total_records:,}")
    col2.metric("Avg. Temperature", f"{avg_temperature:.2f} °C")
    col3.metric("Avg. Humidity", f"{avg_humidity:.2f}%")
    col4.metric("Avg. Wind Speed", f"{avg_wind_speed:.2f} km/h")

    st.divider()
    
# ====================================================
# PAGE 2: TEMPERATURE ANALYSIS
# ====================================================
elif selected_section == "Temperature Analysis":

    st.subheader("Temperature Analysis")

    # Average temperature by month
    monthly_temp = (
        df.groupby("Month", as_index=False)["Temperature (C)"]
        .mean()
    )

    monthly_temp["Month_Name"] = monthly_temp["Month"].map(
        lambda m: month_names[int(m) - 1]
    )

    monthly_temp = monthly_temp.sort_values("Month")

    fig1 = px.line(
        monthly_temp,
        x="Month_Name",
        y="Temperature (C)",
        markers=True,
        category_orders={"Month_Name": month_names},
        labels={
            "Month_Name": "Month",
            "Temperature (C)": "Average Temperature (°C)"
        },
        title="Average Temperature by Month"
    )

    st.plotly_chart(fig1, use_container_width=True)

    # Average temperature by year
    yearly_temp = (
        year_df.groupby("Year", as_index=False)["Temperature (C)"]
        .mean()
    )

    yearly_temp["Year"] = yearly_temp["Year"].astype(str)

    fig2 = px.line(
        yearly_temp,
        x="Year",
        y="Temperature (C)",
        markers=True,
        labels={
            "Year": "Year",
            "Temperature (C)": "Average Temperature (°C)"
        },
        title="Average Temperature by Year"
    )

    st.plotly_chart(fig2, use_container_width=True)

    # Monthly temperature vs apparent temperature
    monthly_comparison = (
        df.groupby("Month", as_index=False)[
            ["Temperature (C)", "Apparent Temperature (C)"]
        ].mean()
    )

    monthly_comparison["Month_Name"] = monthly_comparison["Month"].map(
        lambda m: month_names[int(m) - 1]
    )

    monthly_comparison = monthly_comparison.sort_values("Month")

    comparison_long = monthly_comparison.melt(
        id_vars=["Month_Name"],
        value_vars=[
            "Temperature (C)",
            "Apparent Temperature (C)"
        ],
        var_name="Temperature Type",
        value_name="Temperature"
    )

    comparison_long["Temperature Type"] = (
        comparison_long["Temperature Type"].replace({
            "Temperature (C)": "Actual Temperature",
            "Apparent Temperature (C)": "Apparent Temperature"
        })
    )

    fig3 = px.line(
        comparison_long,
        x="Month_Name",
        y="Temperature",
        color="Temperature Type",
        markers=True,
        category_orders={"Month_Name": month_names},
        labels={
            "Month_Name": "Month",
            "Temperature": "Average Temperature (°C)",
            "Temperature Type": "Measure"
        },
        title="Monthly Temperature vs. Apparent Temperature"
    )

    st.plotly_chart(fig3, use_container_width=True)

# ====================================================
# PAGE 3: PRECIPITATION ANALYSIS
# ====================================================
elif selected_section == "Precipitation Analysis":

    st.subheader("Precipitation Analysis")
    st.caption(
        "This dataset records precipitation type, not rainfall amount."
    )

    precip_counts = (
        df["Precip Type"]
        .fillna("Unknown")
        .replace("", "Unknown")
        .value_counts()
        .rename_axis("Precipitation Type")
        .reset_index(name="Weather Records")
    )

    fig = px.bar(
        precip_counts,
        x="Precipitation Type",
        y="Weather Records",
        text="Weather Records",
        labels={
            "Precipitation Type": "Precipitation Type",
            "Weather Records": "Number of Records"
        },
        title="Precipitation Type Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)
