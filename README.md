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

The first dataset used in this project is the Environmental Protection Agency (EPA) air quality dataset titled “Annual AQI by CBSA (2024).” This dataset was loaded from a CSV file named **annual_aqi_by_cbsa_2024.csv**, which is stored in the project repository (`annual_aqi_by_cbsa_2024.csv`). The file is already in CSV format, which makes it easy to read and process using Python.

In terms of structure, the dataset is organized in a clean tabular format with 501 rows and 18 columns. Each row represents a Core-Based Statistical Area (CBSA), which is essentially a metro area or region. The columns include variables such as the CBSA name, CBSA code, year, and multiple air quality measures. These measures include the number of “Good Days,” “Moderate Days,” and days in different unhealthy categories like “Unhealthy for Sensitive Groups,” “Unhealthy,” “Very Unhealthy,” and “Hazardous.” It also includes summary statistics like maximum AQI, median AQI, and the 90th percentile AQI. All columns are numeric except for the CBSA name, which is a categorical variable.

The content of this dataset focuses on air quality levels across different regions in the United States for the year 2024. One important characteristic is that it breaks down air quality into categories based on the Air Quality Index (AQI), which helps show not just averages but also how often air quality reaches unhealthy levels. Another key feature is that the dataset tracks pollutants such as carbon monoxide (CO), nitrogen dioxide (NO2), ozone, PM2.5, and PM10 by counting how many days each pollutant was the main contributor to poor air quality.

During cleaning, we dropped any missing values and duplicate rows to ensure the dataset was consistent and reliable. Since there were no missing values to begin with, this step mainly confirmed the dataset’s quality. We also checked data types to make sure all numeric fields were properly formatted for analysis.

From an ethical and legal perspective, this dataset comes from a U.S. government agency and is considered public domain, meaning there are no restrictions on its use. There is no personally identifiable information included, so there are no privacy concerns. However, one limitation is that AQI data is based on monitoring stations, which may not fully represent air quality in all areas, especially rural regions.

This dataset directly supports our research questions by allowing us to compare air quality across different regions and identify areas with the best and worst conditions. For example, we can analyze which cities have the highest median AQI or the most unhealthy days. When combined with the crime dataset, it also helps explore whether there are any patterns or relationships between environmental conditions and crime levels.


### Dataset 2: FBI UCR Offenses Known to Law Enforcement by State by City (2024)

**Source:** Federal Bureau of Investigation, Crime Data Explorer
**URL:** https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/downloads
**File:** `crime_cleaned.csv`
**Format:** CSV (cleaned from original Excel)
**License:** Public domain (U.S. government work)

The second dataset used in this project is the FBI’s Uniform Crime Reporting (UCR) data titled “Offenses Known to Law Enforcement by State by City (2024).” This dataset was downloaded from the FBI Crime Data Explorer and then cleaned and saved as a CSV file named **crime_cleaned.csv**. In the project repository, this file is stored as `crime_cleaned.csv`. The original file was in Excel format, but it was converted to CSV after cleaning to make it easier to work with in Python.

In terms of structure, the dataset is organized in a tabular format where each row represents a specific city within a state. The columns include variables such as state, city, population, total violent crime, and specific crime categories like murder, rape, robbery, and aggravated assault. It also includes property crime data, such as burglary, larceny-theft, motor vehicle theft, and arson. After cleaning, the dataset contains around 8,986 rows and 13 main columns, with additional calculated columns like violent crime rate and property crime rate. Most of the variables are numeric, which makes them suitable for statistical analysis, while state and city are categorical identifiers.

The content of the dataset focuses on reported crime counts collected by law enforcement agencies across the United States. One important characteristic of this dataset is that it reports raw counts rather than rates, which means larger cities tend to have higher numbers simply due to population size. That is why we created new variables like crime rates per 100,000 people to allow fair comparisons across cities. Another key characteristic is that the data includes some inconsistencies from the original source, such as missing values and formatting issues, which required cleaning before analysis.

There are also some ethical and legal considerations. Since this dataset comes from a U.S. federal agency, it is in the public domain and does not have restrictions on use or redistribution. There is no personally identifiable information included, so there are no privacy concerns at the individual level. However, there are still limitations to consider. The data only includes crimes that were reported to law enforcement, meaning underreporting is a known issue. This can affect the accuracy of conclusions, especially for crimes that are less likely to be reported.

This dataset directly relates to our research questions because it allows us to analyze patterns in crime across different cities and states. For example, we can compare which states have the highest total violent crime, identify cities with the highest crime levels, and examine which types of crime are most common. Overall, it provides a strong foundation for understanding crime trends at a local and national level.


## Data Quality

### AQI Dataset Quality

(Use class notes for this)

### Crime Dataset Quality

(Use class notes for this)

**Known limitations:** UCR reporting is voluntary and participation rates vary by state. Some states (notably Florida and Illinois historically) have had lower or inconsistent participation. Crime counts are raw totals that require population normalization for fair comparison; we address this by computing per-100,000 crime rates. The UCR counts offenses, not incidents, so a single event with multiple offenses may be counted multiple times.


## Data Cleaning

### AQI Dataset Cleaning

For the AQI dataset, we performed several data cleaning steps to make sure the data was accurate, consistent, and ready for analysis. Even though this dataset was already fairly clean compared to others, we still checked for common issues like missing values, duplicates, and incorrect data types.

First, we loaded the dataset and inspected the structure using `.head()`, `.shape`, and `.dtypes`. This helped us understand how the data was organized and confirm that each column matched its expected type. We found that most of the columns were already correctly formatted as integers or objects, which reduced the amount of heavy cleaning needed.

Next, we checked for missing values using `df.isnull().sum()`. This step is important because missing data can affect calculations like averages or comparisons across cities. In this dataset, all columns showed zero missing values, which means the dataset was already complete. Even though no imputation was needed, doing this check helped confirm data quality and reliability.

We also removed duplicate rows using `df.drop_duplicates()`. Duplicate entries can inflate results and create bias, especially when calculating averages or identifying trends across cities. By removing duplicates, we ensured that each CBSA was only represented once per year, keeping the dataset accurate and preventing overcounting.

After cleaning, we verified the dataset structure again using `df.shape` and found that it contained 501 rows and 18 columns. This confirmed that no important data was accidentally removed during cleaning. We also rechecked data types to make sure all AQI-related variables (like “Good Days,” “Moderate Days,” and “Median AQI”) remained numeric. This was important because numeric formatting is required for calculations such as means, grouping, and comparisons.

We also created a quick validation step by checking summary statistics using `df.describe()`. This helped us confirm that the values made sense logically, such as “Good Days” being much higher than “Hazardous Days,” which matches expectations for air quality data.

Overall, the cleaning process focused more on verification than heavy transformation. The main goal was to ensure there were no missing values, no duplicate records, and that all variables were correctly formatted for analysis. These steps improved the reliability of the dataset and made it suitable for comparing air quality across different regions and identifying patterns in AQI distribution.


### Crime Dataset Cleaning

In this project, we performed several data cleaning steps to turn the Crime Excel dataset into something usable for analysis. Each step was meant to fix a specific data quality issue that would have caused problems later.

First, we adjusted how the file was read in by skipping the first four rows. The original dataset had extra header information and notes at the top, which were not part of the actual data. If we did not skip these rows, the columns would be misaligned and difficult to work with. After that, we manually renamed all the columns to clear and consistent names. This made the dataset easier to understand and allowed us to reference columns without confusion.

Next, we removed rows where the city value was missing. These rows did not represent real observations, so keeping them would have added unnecessary noise. Another issue we noticed was that the “state” column had missing values for many rows. This happened because the dataset only listed the state name once for a group of cities. To fix this, we filled the missing state values downward so that each city had the correct state attached.

We then converted all numeric columns, such as population and crime counts, into proper numeric data types. Some values were likely read as text, which would prevent calculations from working correctly. By converting these columns and forcing errors to become null values, we ensured consistency across the dataset.

After that, we dropped rows that were still missing key values like population or violent crime. These fields are important for analysis, so rows without them would not be useful. We also reset the index to keep the dataset clean and organized after removing rows.

Finally, we created new variables such as violent crime rate and property crime rate. This step was important because raw counts can be misleading when comparing cities of different sizes. By standardizing crime per 100,000 people, the data became more meaningful.

Overall, these cleaning steps improved accuracy, consistency, and usability, making the dataset reliable for further analysis.


### Merge Strategy

For the merge strategy, we combined the AQI dataset and the crime dataset to analyze potential relationships between air quality and crime levels across cities. Since the two datasets did not originally share a common key, we had to create a shared variable to make the merge possible.

First, we extracted a “city” column from the AQI dataset by splitting the CBSA field. The CBSA column contained both the metro area name and state abbreviation, so we split it by commas and hyphens to isolate only the city name. We then cleaned it by stripping extra spaces and converting all text to lowercase. We applied the same cleaning process to the city column in the crime dataset. This step was important to standardize formatting and avoid mismatches during merging.

After standardizing the city names, we used an inner merge on the “city” column. We chose an inner join because we only wanted records that existed in both datasets, ensuring that the final dataset contained complete information for both air quality and crime variables.

The result was a merged dataset that combines AQI metrics (like median AQI and number of good days) with crime statistics (such as violent crime and property crime). This allowed us to analyze both environmental conditions and public safety indicators together at the city level.


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
