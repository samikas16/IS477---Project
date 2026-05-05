import pandas as pd
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--aqi")
    parser.add_argument("--crime")
    parser.add_argument("--out")
    args = parser.parse_args()

    aqi_df = pd.read_csv(args.aqi)
    crime_df = pd.read_csv(args.crime)

    aqi_df["city"] = aqi_df["CBSA"].str.split(",").str[0]
    aqi_df["city"] = aqi_df["city"].str.split("-").str[0]
    aqi_df["city"] = aqi_df["city"].str.strip().str.lower()

    crime_df["city"] = crime_df["city"].str.strip().str.lower()
    aqi_df = aqi_df.drop_duplicates(subset=["city"])
    crime_df = crime_df.drop_duplicates(subset=["city"])

    merged = pd.merge(aqi_df, crime_df, on="city", how="inner")

    merged.to_csv(args.out, index=False)

    print(f"Merged dataset saved to {args.out}")
    print(f"Final shape: {merged.shape}")

if __name__ == "__main__":
    main()
