# 🌦️ Weather History & Seasonal Pattern Analysis

## 📌 Project Overview

**Weather History & Seasonal Pattern Analysis** is a Python-based data analysis project that explores historical weather observations to understand seasonal temperature patterns, year-to-year temperature variations, differences between measured and apparent temperature, and the distribution of recorded precipitation types.

The project uses **Python, Pandas, Plotly, and Streamlit** to clean weather data, calculate key performance indicators (KPIs), analyse historical patterns, and present the findings through an interactive dashboard.

The analysis focuses on four strongly supported visualizations and recommendations that can be directly justified by the available data.

## 🎯 Business Objective

The main objectives of this project are to:

* Understand how average temperature changes across the months of the year.
* Compare average temperatures across years with sufficient observations.
* Examine differences between measured temperature and apparent temperature.
* Understand the distribution of recorded precipitation classifications.
* Summarize key weather metrics through dashboard KPIs.
* Translate supported observations into practical, data-informed recommendations.

## 🧰 Tools and Technologies

* **Python** — data analysis and calculations
* **Pandas** — data cleaning, transformation, and aggregation
* **Plotly** — interactive data visualizations
* **Streamlit** — interactive dashboard development
* **GitHub** — project version control and documentation

## 📂 Dataset Overview

The project uses historical weather observations containing temperature, apparent temperature, humidity, wind speed, visibility, precipitation type, and date-related information.

### Original Dataset

* File: `weatherHistory.csv`
* Rows: 96,453
* Columns: 12

### Cleaned Dataset

* File: `weather_history_cleaned.csv`
* Rows: 96,429
* Columns: 17

### Data Cleaning and Preparation

The data preparation process included:

1. Loading and inspecting the original dataset.
2. Parsing the formatted date column into a usable datetime format.
3. Removing 24 duplicate records.
4. Creating additional time-based features: `Year`, `Month`, `Month_Name`, `Day`, and `Hour`.
5. Preparing the cleaned dataset for aggregation, analysis, and visualization.
6. Preserving the `Unknown` precipitation category instead of assuming its classification.

The cleaned dataset contains 96,429 records and is used for the dashboard's KPIs and visualizations.

## 📊 Key Performance Indicators (KPIs)

The Executive Dashboard displays four KPIs calculated from `weather_history_cleaned.csv`.

| KPI                   | Python Formula                   |     Result |
| --------------------- | -------------------------------- | ---------: |
| Total Weather Records | `len(df)`                        |     96,429 |
| Average Temperature   | `df["Temperature (C)"].mean()`   |    11.93°C |
| Average Humidity      | `df["Humidity"].mean() * 100`    |     73.49% |
| Average Wind Speed    | `df["Wind Speed (km/h)"].mean()` | 10.81 km/h |

### 1. Total Weather Records

```python
total_records = len(df)
```

Counts the total number of rows in the cleaned dataset, resulting in **96,429 weather records**.

### 2. Average Temperature

```python
avg_temperature = df["Temperature (C)"].mean()
```

Calculates the arithmetic mean of the `Temperature (C)` column, resulting in an average temperature of **11.93°C**.

### 3. Average Humidity

```python
avg_humidity = df["Humidity"].mean() * 100
```

Calculates the mean of the `Humidity` column and multiplies it by 100 to convert the decimal fraction into a percentage, resulting in **73.49% average humidity**.

### 4. Average Wind Speed

```python
avg_wind_speed = df["Wind Speed (km/h)"].mean()
```

Calculates the arithmetic mean of the `Wind Speed (km/h)` column, resulting in an average wind speed of **10.81 km/h**.

**KPI notes:**

* Temperature is measured in degrees Celsius.
* Humidity is stored as a decimal fraction and converted into a percentage for display.
* Wind speed is measured in kilometres per hour.
* Total weather records represent rows in the dataset, not necessarily unique days or individual weather events.

The detailed calculations and explanations are documented in `KPI_Calculations.docx`.

## 📈 Dashboard Structure

The dashboard contains three main sections.

### 1. Executive Dashboard

Displays four KPI cards:

* Total Weather Records
* Average Temperature
* Average Humidity
* Average Wind Speed

### 2. Temperature Analysis

Contains three retained visualizations:

* Average Temperature by Month
* Average Temperature by Year
* Monthly Temperature vs. Apparent Temperature

### 3. Precipitation Analysis

Contains one retained visualization:

* Precipitation Type Distribution

The dashboard retains only the four visualizations assessed as **strongly supported** for their stated observations and bounded recommendations.

## 🔍 Visualization Analysis and Recommendation Justification

Each retained visualization follows this framework:

**Business Question → Observation → Insight → Recommendation → Data Support**

### Visualization 1: Average Temperature by Month

**Business Question:** How does average temperature vary throughout the year?

**Observation:**

* July records the highest average temperature at approximately **22.97°C**.
* January records the lowest average temperature at approximately **0.82°C**.
* The difference between these monthly averages is approximately **22.15°C**.

**Insight:** The monthly averages show a clear seasonal temperature pattern, with warmer mid-year months and colder winter months.

**Recommendation:** Use historical monthly temperature patterns as a reference when planning weather-sensitive activities and seasonal operations.

**Why the recommendation is justified:** The visualization directly compares average temperatures across all twelve months. It supports identifying warmer and colder periods and using those historical patterns for planning. It does not, by itself, establish the impact on costs, demand, or operational performance.

### Visualization 2: Average Temperature by Year

**Business Question:** How did average temperature vary across the observed years?

**Observation:**

* Among the years 2006–2016, 2014 records the highest annual average temperature at approximately **12.53°C**.
* 2010 records the lowest annual average temperature at approximately **11.17°C**.
* The difference between these annual averages is approximately **1.36°C**.

**Insight:** Annual average temperatures vary across the observed years. The comparison describes year-to-year variation but does not, on its own, establish a long-term climate trend.

**Recommendation:** Use annual temperature averages to compare historical conditions and investigate year-to-year variations.

**Why the recommendation is justified:** The visualization directly compares annual average temperatures and identifies the highest and lowest values within the selected comparison period. The 2005 observation is excluded from annual comparisons because that year contains only one record, making its average unsuitable for a meaningful comparison with years containing substantially more observations.

### Visualization 3: Monthly Temperature vs. Apparent Temperature

**Business Question:** How does measured temperature compare with apparent temperature throughout the year?

**Observation:**

* In January, average measured temperature is approximately **0.82°C**.
* Average apparent temperature in January is approximately **−1.94°C**.
* Apparent temperature is therefore approximately **2.75°C lower** than measured temperature in January.
* The two measures are relatively close during much of the April–September period.

**Insight:** Measured temperature and apparent temperature do not always match. The difference is particularly noticeable in colder months.

**Recommendation:** Consider both measured and apparent temperatures when planning weather-sensitive outdoor activities.

**Why the recommendation is justified:** The visualization directly compares the two temperature measures across the months of the year. It supports considering both values when reviewing historical weather conditions, without claiming that the comparison alone predicts safety outcomes or specific weather impacts.

### Visualization 4: Precipitation Type Distribution

**Business Question:** What proportion of recorded weather observations is classified as rain, snow, or unknown?

**Observation:**

| Precipitation Type |    Records |  Percentage |
| ------------------ | ---------: | ----------: |
| Rain               |     85,200 |      88.35% |
| Snow               |     10,712 |      11.11% |
| Unknown            |        517 |       0.54% |
| **Total**          | **96,429** | **100.00%** |

**Insight:** Rain is the predominant recorded precipitation classification in the dataset, while a small proportion of records have an unknown classification.

**Recommendation:** Use the recorded precipitation-type distribution to summarize historical conditions while retaining the unknown category in reporting.

**Why the recommendation is justified:** The visualization directly represents the frequency and proportion of each recorded precipitation classification. Keeping the unknown category visible avoids incorrectly assigning those records to rain or snow.

**Important limitation:** These percentages describe dataset records, not the percentage of rainy days, rainfall volume, or precipitation intensity. The dataset does not contain a numeric rainfall-amount field for those calculations.

## 🧠 Key Findings

The analysis identifies the following data-supported findings:

* July has the highest average monthly temperature, at approximately 22.97°C.
* January has the lowest average monthly temperature, at approximately 0.82°C.
* Among 2006–2016, 2014 has the highest annual average temperature and 2010 the lowest.
* Apparent temperature is lower than measured temperature in January, illustrating a difference between the two measures.
* Rain accounts for 88.35% of recorded precipitation classifications, snow for 11.11%, and unknown classifications for 0.54%.

These findings describe the analyzed dataset and should not be interpreted as forecasts or proof of long-term climate change.

## 💼 Business Relevance

Although the project analyses weather rather than business transactions, its findings can help demonstrate how data analysis supports evidence-based planning.

Potential uses include:

* Referencing historical monthly temperatures when planning seasonal activities.
* Comparing annual averages to identify years that merit further investigation.
* Reviewing measured and apparent temperatures when considering outdoor activities.
* Summarizing historical precipitation classifications while communicating data limitations clearly.

These are general planning applications. The dataset does not directly measure business costs, customer demand, operational outcomes, rainfall volume, or the effectiveness of any recommendation.

## 📁 Repository Structure

```text
weather-history-seasonal-pattern-analysis/
│
├── app.py
├── requirements.txt
├── weather_history_cleaned.csv
├── Dashboard_GIF_Screenshots.gif
├── KPI_Calculations.docx
├── Recommendation_Justification.docx
└── README.md
```

### Supporting Documentation

**`KPI_Calculations.docx`**

Documents the four KPI formulas, calculated results, and explanations of how each KPI is derived from the cleaned dataset.

**`Recommendation_Justification.docx`**

Documents the business question, observation, insight, recommendation, and justification for each of the four retained visualizations. It explains why the recommendations are supported by the available data and identifies relevant limitations.

**`Dashboard_GIF_Screenshots.gif`**

Provides a visual preview of the dashboard.

## ▶️ How to Run the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/yashjsri-hue/weather-history-seasonal-pattern-analysis.git
```

### 2. Open the Project Folder

```bash
cd Weather_and_Rainfall_Pattern_Analysis
```

### 3. Install the Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Dashboard

```bash
py -m streamlit run app.py
```

The dashboard should open in your browser through the local Streamlit server.

## 📦 Dependencies

The project uses the following Python packages:

```text
streamlit
pandas
plotly
```

## ⚠️ Limitations

* The analysis is descriptive and focuses on historical observations.
* The 2005 annual average is excluded from annual comparisons because it is based on only one record.
* Precipitation percentages represent recorded classifications, not rainfall amounts or the proportion of rainy days.
* The unknown precipitation category is retained rather than reclassified without evidence.
* The findings do not independently establish long-term climate trends or causal relationships.
* Business recommendations are limited to actions that can reasonably be supported by the available weather data.

## ✅ Conclusion

Weather History & Seasonal Pattern Analysis demonstrates a complete workflow for preparing historical data, calculating KPIs, exploring seasonal and annual temperature patterns, comparing measured and apparent temperature, and examining precipitation classifications.

By retaining four strongly supported visualizations and documenting the reasoning behind their recommendations, the project emphasizes clear analysis, evidence-based interpretation, and transparent communication of data limitations.

The two supporting Word documents provide the calculation details and recommendation justifications needed to make the project more transparent, reproducible, and suitable for a data analyst portfolio.

## 👤 Author

**Yash Srivastava**

Python | Pandas | Plotly | Streamlit | Data Analysis | Data Visualization
