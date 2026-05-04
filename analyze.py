import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns



merged = pd.read_csv("merged_aqi_crime.csv")

# Statistics

merged["aqi_quartile"] = pd.cut(merged["Median AQI"], 4,labels=["Q1 (Best)", "Q2", "Q3", "Q4 (Worst)"])
q_summary = merged.groupby("aqi_quartile")[["violent_crime_rate","property_crime_rate"]].mean()
top5 = merged[["CBSA","Median AQI","violent_crime_rate","property_crime_rate"]].sort_values("Median AQI", ascending=False).head(5)

lines = ["Analysis Summary: Air Quality vs. Crime (2024)", f"Merged dataset: {len(merged)} city-level observations","", "Average Crime Rates by AQI Quartile", q_summary.to_string(), "", "Top 5 Cities by Median AQI", top5.to_string(index=False),]

#Visualizations

fig, axes = plt.subplots(2, 2, figsize=(14, 11))
fig.suptitle("Air Quality vs. Crime Rates Across U.S. Cities (2024)",fontsize=16, fontweight="bold", y=1.01)

ax = axes[0, 0]
ax.scatter(merged["Median AQI"], merged["violent_crime_rate"], alpha=0.5, color="steelblue", s=30)
ax.set_xlabel("Median AQI"); ax.set_ylabel("Violent Crime Rate (per 100k)")
ax.set_title(f"Median AQI vs Violent Crime Rate\n")

ax = axes[0, 1]
ax.scatter(merged["Median AQI"], merged["property_crime_rate"], alpha=0.5, color="darkorange", s=30)
ax.set_xlabel("Median AQI"); ax.set_ylabel("Property Crime Rate (per 100k)")
ax.set_title(f"Median AQI vs Property Crime Rate\n")

ax = axes[1, 0]
ax.bar(["Q1 (Best)", "Q2", "Q3", "Q4 (Worst)"], q_summary["violent_crime_rate"], 0.35, label="Violent Crime", color="steelblue")
ax.bar(["Q1 (Best)", "Q2", "Q3", "Q4 (Worst)"], q_summary["property_crime_rate"], 0.35, label="Property Crime", color="darkorange")
ax.set_ylabel("Avg Crime Rate (per 100k)")
ax.set_title("Crime Rates by AQI Quartile")
ax.legend()

ax = axes[1, 1]
merged["crime_group"] = pd.cut(merged["violent_crime_rate"], 3,labels=["Low", "Mid", "High"])
merged.boxplot(column="Good Days", by="crime_group", ax=ax)
ax.set_xlabel("Violent Crime Level")
ax.set_ylabel("Good Air Quality Days")
plt.sca(ax)
plt.title("Good AQI Days by Crime Level")

plt.show()

