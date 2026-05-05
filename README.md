# IS477---Project
# Air Quality and Crime: Exploring Environmental and Social Patterns Across U.S. Cities (2024)

## Contributors
- Sreeja Nallamala
- Samika Sripathi

## Summary

This project investigates whether a relationship exists between air pollution levels and crime rates across cities in the United States using 2024 data. Environmental quality and public safety are two concerns that frequently intersect in policy discussions, yet empirical analysis of their co-occurrence at the city level is limited. Our core research questions were:Is there a measurable relationship between air pollution levels and crime rates across U.S. cities? Does pollution relate differently to violent crime versus property crime? Are there regional patterns where high pollution and high crime co-occur? To answer these questions, we merged the EPA's annual Air Quality Index (AQI) dataset for 2024 with the FBI's Uniform Crime Reporting (UCR) dataset for 2024, which records offenses known to law enforcement by city. Our analysis found a statistically significant positive correlation between Median AQI and violent crime rate, meaning cities with worse air quality tended to report higher violent crime rates per capita. 

## Data Profile

### Dataset 1: EPA Annual AQI by CBSA (2024)

**Source:** U.S. Environmental Protection Agency, Air Quality System (AQS)
**URL:** https://aqs.epa.gov/aqsweb/airdata/download_files.html#Annual
**File:** `annual_aqi_by_cbsa_2024.csv`
**Format:** CSV
**License:** Public domain (U.S. government work)

### Dataset 2: FBI UCR Offenses Known to Law Enforcement by State by City (2024)

**Source:** Federal Bureau of Investigation, Crime Data Explorer
**URL:** https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/downloads
**File:** `crime_cleaned.csv`
**Format:** CSV (cleaned from original Excel)
**License:** Public domain (U.S. government work)

**Ethical considerations:** Both datasets are published by U.S. federal agencies and are in the public domain with no redistribution restrictions. The crime data reflects reported offenses only; underreporting is a known limitation of UCR data. No personally identifiable information is present in either dataset. 

## Data Quality

### AQI Dataset Quality

(Use class notes for this)

### Crime Dataset Quality

(Use class notes for this)

**Known limitations:** UCR reporting is voluntary and participation rates vary by state. Some states (notably Florida and Illinois historically) have had lower or inconsistent participation. Crime counts are raw totals that require population normalization for fair comparison; we address this by computing per-100,000 crime rates. The UCR counts offenses, not incidents, so a single event with multiple offenses may be counted multiple times.


## Data Cleaning

### AQI Dataset Cleaning

The AQI dataset required minimal cleaning. The primary operation was extracting a matchable city name from the CBSA field for merging purposes. CBSA names follow the format "PrimaryCity-SecondaryCity, StateAbbrev(s)", so we split on the comma to isolate the city portion, then split on the hyphen to take only the primary city name, and finally applied .str.strip().str.lower() to standardize case and remove whitespace. 

### Crime Dataset Cleaning

The crime dataset cleaning involved several steps. First, we skipped the first 4 rows of the Excel file, which contained title and formatting content rather than data. Second, we manually assigned column names to replace the default multi-level header. Third, we dropped rows where the city column was null, as these were formatting artifacts. Fourth, we forward-filled the state column to propagate state names across the blank rows that followed the first city in each state group. Fifth, we converted all numeric columns using pd.to_numeric(errors='coerce') to handle footnote characters and formatting symbols that appeared in some cells.
### Merge Strategy

To merge the two datasets, we standardized city names from both and performed an inner join on the city field. The inner join retained only cities present in both datasets. Of 501 AQI metro areas and 6,892 unique city names in the crime data, the city matches were retained in the final merged dataset.

## Findings

(We will write later)

## Future Work

(We will write later)

## Challenges

(We will write later)

## Reproducing


1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd IS477-Project
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the raw datasets**:
   - AQI: https://aqs.epa.gov/aqsweb/airdata/annual_aqi_by_cbsa_2024.zip
   - Crime: https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/downloads

4. **Verify checksums:**
   ```
   annual_aqi_by_cbsa_2024.csv: 548c45b5b8822f5bcd988a17ea55726134ca668b82151c418ce3f7b3b2663cff
   crime_cleaned.csv:           9ede2384558c90fe0a5b22d68ae41d2449755d0d6de7dad64681ea0d297dd0b8
   ```

5. **Run the full pipeline using Snakemake:**
   ```bash
   snakemake --cores 1
   ```

6. **Or run notebooks manually in order:**
   - `CrimeDataset.ipynb` — cleans the raw Excel file and saves `crime_cleaned.csv`
   - `EnvironmentDataset.ipynb` — exploratory analysis of AQI data
   - `merge.ipynb` — merges the two datasets
   - `analysis.py` — generates statistics

**Expected outputs:** `merged_aqi_crime.csv`


## References

Federal Bureau of Investigation. (2024). *Crime in the United States 2024: Offenses Known to Law Enforcement by State by City*. FBI Crime Data Explorer. https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/downloads

U.S. Environmental Protection Agency. (2024). *Annual Summary of Air Quality Index (AQI) Statistics by Core Based Statistical Area (CBSA), 2024*. Air Quality System Data Mart. https://aqs.epa.gov/aqsweb/airdata/download_files.html#Annual
