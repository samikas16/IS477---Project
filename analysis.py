import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

rq   = "annual_aqi_by_cbsa_2024.csv"
rc = "crime_cleaned.csv"
m = "merged_aqi_crime.csv"


aqi_df   = pd.read_csv(rq)
crime_df = pd.read_csv(rc)

# Cleaning
aqi_df["city"] = (aqi_df["CBSA"].str.split(",").str[0].str.split("-").str[0].str.strip().str.lower())
crime_df["city"] = crime_df["city"].str.strip().str.lower()

# Compute crime rates er-capita
crime_df["violent_crime_rate"]  = (crime_df["violent_crime"]  / crime_df["population"]) * 100000
crime_df["property_crime_rate"] = (crime_df["property_crime"] / crime_df["population"]) * 100000

# Group crime to city level
crime_agg = (crime_df.groupby("city").agg(
        population          = ("population",          "sum"),      
        violent_crime       = ("violent_crime",       "sum"),
        property_crime      = ("property_crime",      "sum"), 
        murder              = ("murder",              "sum"),
        rape                = ("rape",                "sum"),
        robbery             = ("robbery",             "sum"),
        aggravated_assault  = ("aggravated_assault",  "sum"),
        burglary            = ("burglary",            "sum"),
        larceny_theft       = ("larceny_theft",       "sum"),
        motor_vehicle_theft = ("motor_vehicle_theft", "sum"),
        arson               = ("arson",               "sum"),
    )
    .reset_index()
)
crime_agg["violent_crime_rate"]  = (crime_agg["violent_crime"]  / crime_agg["population"]) * 100_000
crime_agg["property_crime_rate"] = (crime_agg["property_crime"] / crime_agg["population"]) * 100_000

# Merge
merged = pd.merge(aqi_df, crime_agg, on="city", how="inner")
merged = merged[merged["population"] > 0].copy()
merged.to_csv(m, index=False)


#Visualizations
fig, axes = plt.subplots(2, 2, figsize=(14, 11))
fig.suptitle("Air Quality vs. Crime Rates Across U.S. Cities (2024)", fontsize=16, fontweight="bold", y=1.01)

# 1. Median AQI vs Violent Crime Rate
ax = axes[0, 0]
ax.scatter(merged["Median AQI"], merged["violent_crime_rate"],
           alpha=0.5, color="steelblue", s=30)
m, b = np.polyfit(merged["Median AQI"], merged["violent_crime_rate"], 1)
x_line = np.linspace(merged["Median AQI"].min(), merged["Median AQI"].max(), 100)
ax.plot(x_line, m * x_line + b, color="crimson", linewidth=2)
ax.set_xlabel("Median AQI")
ax.set_ylabel("Violent Crime Rate (per 100k)")
ax.set_title("Median AQI vs Violent Crime Rate")

# 2. Median AQI vs Property Crime Rate
ax = axes[0, 1]
ax.scatter(merged["Median AQI"], merged["property_crime_rate"],alpha=0.5, color="darkorange", s=30)
m2, b2 = np.polyfit(merged["Median AQI"], merged["property_crime_rate"], 1)
ax.plot(x_line, m2 * x_line + b2, color="crimson", linewidth=2)
ax.set_xlabel("Median AQI")
ax.set_ylabel("Property Crime Rate (per 100k)")
ax.set_title("Median AQI vs Property Crime Rate")

# 3. Crime rates by AQI quartile

ax = axes[1, 0]
merged["aqi_quartile"] = pd.qcut(merged["Median AQI"], 4,labels=["Q1 (Best)", "Q2", "Q3", "Q4 (Worst)"])
ax = axes[1, 0]
q_data = merged.groupby("aqi_quartile")[["violent_crime_rate", "property_crime_rate"]].mean()
x = np.arange(len(q_data))
w = 0.35
ax.bar(x - w/2, q_data["violent_crime_rate"],  w, label="Violent Crime",  color="steelblue")
ax.bar(x + w/2, q_data["property_crime_rate"], w, label="Property Crime", color="darkorange")
ax.set_xticks(x)
ax.set_xticklabels(["Q1\n(Best AQI)", "Q2", "Q3", "Q4\n(Worst AQI)"])
ax.set_ylabel("Avg Crime Rate (per 100k)")
ax.set_title("Average Crime Rates by AQI Quartile")
ax.legend()

# 4. Good Days by crime
ax = axes[1, 1]
merged["crime_tertile"] = pd.qcut(
    merged["violent_crime_rate"], 3,
    labels=["Low Crime", "Mid Crime", "High Crime"]
)
merged.boxplot(
    column="Good Days", by="crime_tertile", ax=ax,
    boxprops=dict(color="steelblue"),
    medianprops=dict(color="crimson", linewidth=2)
)
ax.set_xlabel("Violent Crime Tertile")
ax.set_ylabel("Good Air Quality Days")
plt.sca(ax)
plt.title("Good AQI Days by Crime Level")
plt.show()

