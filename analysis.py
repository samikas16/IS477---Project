import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

aqi_df   = pd.read_csv("annual_aqi_by_cbsa_2024.csv")
crime_df = pd.read_csv("crime_cleaned.csv")

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
merged.to_csv("merged_aqi_crime.csv", index=False)


#Visualizations
fig, axes = plt.subplots(2, 2, figsize=(14, 11))
fig.suptitle("Air Quality vs. Crime Rates Across U.S. Cities (2024)", fontsize=16, fontweight="bold", y=1.01)

# 1. Median AQI vs Violent Crime Rate
ax = axes[0, 0]
ax.scatter(merged["Median AQI"], merged["violent_crime_rate"], alpha=0.5, color="steelblue", s=30)
ax.set_xlabel("Median AQI"); ax.set_ylabel("Violent Crime Rate (per 100k)")
ax.set_title(f"Median AQI vs Violent Crime Rate\n")

# 2. Median AQI vs Property Crime Rate
ax = axes[0, 1]
ax.scatter(merged["Median AQI"], merged["property_crime_rate"], alpha=0.5, color="darkorange", s=30)
ax.set_xlabel("Median AQI"); ax.set_ylabel("Property Crime Rate (per 100k)")
ax.set_title(f"Median AQI vs Property Crime Rate\n")

# 3. Crime rates by AQI quartile

ax = axes[1, 0]
merged["aqi_quartile"] = pd.qcut(merged["Median AQI"], 4, labels=["Q1 (Best)", "Q2", "Q3", "Q4 (Worst)"])
q_data = merged.groupby("aqi_quartile")[["violent_crime_rate", "property_crime_rate"]].mean()
q_data.plot(kind="bar", ax=ax, color=["steelblue", "darkorange"], rot=0)
ax.set_xlabel("")
ax.set_ylabel("Avg Crime Rate (per 100k)")
ax.set_title("Crime Rates by AQI Quartile")
ax.legend(["Violent Crime", "Property Crime"])

# 4. Good Days by crime
ax = axes[1, 1]
merged["crime_group"] = pd.cut(merged["violent_crime_rate"], 3,labels=["Low", "Mid", "High"])
merged.boxplot(column="Good Days", by="crime_group", ax=ax)
ax.set_xlabel("Violent Crime Level")
ax.set_ylabel("Good Air Quality Days")
plt.sca(ax)
plt.title("Good AQI Days by Crime Level")
plt.show()

