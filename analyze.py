import argparse
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--merged", default="merged_aqi_crime.csv")
args = parser.parse_args()

merged = pd.read_csv(args.merged)
merged = merged[merged["population"] > 0].copy()

merged["violent_crime_rate"] = (merged["violent_crime"] / merged["population"]) * 100000
merged["property_crime_rate"] = (merged["property_crime"] / merged["population"]) * 100000

merged["aqi_quartile"] = pd.qcut(merged["Median AQI"], 4, labels=["Q1 (Best)", "Q2", "Q3", "Q4 (Worst)"])
q_summary = merged.groupby("aqi_quartile")[["violent_crime_rate", "property_crime_rate"]].mean()
top5 = merged[["CBSA", "Median AQI", "violent_crime_rate", "property_crime_rate"]].sort_values("Median AQI", ascending=False).head(5)

with open("analysis_output.txt", "w") as f:
    f.write("ANALYSIS SUMMARY: AIR QUALITY VS CRIME (2024)\n\n")
    f.write(f"Observations: {len(merged)}\n\n")
    f.write("Average Crime Rates by AQI Quartile:\n")
    f.write(q_summary.to_string())
    f.write("\n\nTop 5 Cities by Worst AQI:\n")
    f.write(top5.to_string(index=False))

plt.figure()
plt.scatter(merged["Median AQI"], merged["violent_crime_rate"], alpha=0.5)
plt.xlabel("Median AQI")
plt.ylabel("Violent Crime Rate (per 100k)")
plt.title("AQI vs Violent Crime Rate")
plt.savefig("plot1_aqi_violent.png", bbox_inches="tight")
plt.close()

plt.figure()
plt.scatter(merged["Median AQI"], merged["property_crime_rate"], alpha=0.5, color="darkorange")
plt.xlabel("Median AQI")
plt.ylabel("Property Crime Rate (per 100k)")
plt.title("AQI vs Property Crime Rate")
plt.savefig("plot2_aqi_property.png", bbox_inches="tight")
plt.close()

plt.figure()
q_summary.plot(kind="bar", color=["steelblue", "darkorange"])
plt.ylabel("Crime Rate per 100k")
plt.title("Crime Rates by AQI Quartile")
plt.xticks(rotation=0)
plt.savefig("plot3_quartiles.png", bbox_inches="tight")
plt.close()

plt.figure()
merged.boxplot(column="Good Days", by="aqi_quartile")
plt.title("Good Air Quality Days by AQI Quartile")
plt.suptitle("")
plt.xlabel("AQI Quartile")
plt.ylabel("Good Days")
plt.savefig("plot4_boxplot.png", bbox_inches="tight")
plt.close()