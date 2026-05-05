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

First, we extracted a “city” column from the AQI dataset by splitting the CBSA field. The CBSA column contained both the metro area name and state abbreviation, so we split it by commas and hyphens to isolate only the city name. We then cleaned it by stripping extra spaces and converting all text to lowercase. We also made sure to drop duplicate cities for both datasets in separate ways. We applied the same cleaning process to the city column in the crime dataset. This step was important to standardize formatting and avoid mismatches during merging.

After standardizing the city names, we used an inner merge on the “city” column. We chose an inner join because we only wanted records that existed in both datasets, ensuring that the final dataset contained complete information for both air quality and crime variables.

The result was a merged dataset that combines AQI metrics (like median AQI and number of good days) with crime statistics (such as violent crime and property crime). This allowed us to analyze both environmental conditions and public safety indicators together at the city level.


## Findings

The EPA air quality dataset had 501 city-level observations across the United States for 2024. The median AQI ranged from 3 to 97, with a mean of 41 and a standard deviation of 11, which shows that most cities had relatively moderate air quality for the year. On average, cities had 237 good air quality days, so for most cities, the majority of days had acceptable air quality. The highest single-day AQI recorded was 1,513, which is way above the hazardous threshold and was probably caused by a major wildfire or pollution event somewhere in the country.

The FBI crime dataset had 8,986 city-level observations across the United States for 2024. Violent crime rates ranged from 0 to 50,000 per 100,000 residents, with a mean of 249 and a median of 148, so most cities actually have pretty low violent crime but a few extreme outliers are pulling the average up. Property crime rates ranged from 0 to 1,375,000 per 100,000 residents, with a mean of 1,664 and a median of 1,002.

After merging the two datasets we ended up with 463 city-level observations. The merged dataset had a median AQI ranging from 7 to 97, a mean violent crime rate of 490 per 100,000, and a mean property crime rate of 2,379 per 100,000. We then split cities into four quartile groups by median AQI. Q1 cities (best air quality) averaged a violent crime rate of 389 and a property crime rate of 2,163 per 100,000. Q2 averaged 406 violent and 2,131 property crimes per 100,000. Q3 jumped to 525 violent and 2,425 property crimes per 100,000. Q4 cities (worst air quality) averaged 648 violent and 2,824 property crimes per 100,000. That is a 66% increase in violent crime and a 31% increase in property crime just going from the cleanest to the most polluted group. The bar chart makes this trend pretty obvious, with both crime types climbing steadily from Q1 to Q4 and property crime rates consistently much higher than violent crime across every quartile.


<img width="1164" height="908" alt="image" src="https://github.com/user-attachments/assets/864c2232-aefa-4538-8495-930540607093" />


<img width="586" height="455" alt="image" src="https://github.com/user-attachments/assets/9ba5b949-4faa-4def-b9ff-8735186ee0f5" />


<img width="580" height="455" alt="image" src="https://github.com/user-attachments/assets/670bc651-ba7e-4241-92d6-4fa941817b4e" />


<img width="587" height="445" alt="image" src="https://github.com/user-attachments/assets/5456d604-d2c0-4bf3-99c2-01bd1699d7e4" />



The five cities with the worst air quality were Riverside-San Bernardino, CA (97), Phoenix-Mesa-Scottsdale, AZ (86), Bakersfield, CA (72), Visalia-Porterville, CA (71), and San Diego, CA (71), all in California or Arizona. Their violent crime rates were pretty spread out though, with Phoenix being the highest at 797 per 100,000 and San Diego the lowest at 412. All five had above-average property crime rates compared to the full dataset mean of 2,379.

The five cities with the highest violent crime rates were Memphis, TN (2,489 per 100,000), Detroit, MI (1,781), Atlantic City, NJ (1,780), Little Rock, AR (1,672), and Americus, GA (1,654). Interestingly, none of these cities had the worst air quality, which suggests that crime is driven by a lot more than just pollution. This shows up in the scatter plots too, where there is a huge spread in crime rates at every AQI level, so there is clearly no simple linear relationship between the two variables.

The boxplot of good air quality days by AQI quartile shows a pretty clear pattern, with Q1 cities having a median of around 305 good days per year, Q2 around 270, Q3 around 235, and Q4 only about 165. When we looked at crime groups instead, low crime cities averaged 239 good air quality days, mid crime cities averaged 208, and high crime cities averaged only 164. So cities with cleaner air do tend to have lower crime, but this probably has more to do with underlying socioeconomic factors than air quality directly causing or preventing crime.

Overall there is a noticeable trend where cities with worse air quality tend to have higher crime rates, but it is not a clean relationship. A lot of high crime cities have perfectly moderate air quality, which points to poverty, population density, and urban inequality being the real drivers behind both outcomes at the same time.

## Future Work

This project gave us a lot of hands-on experience working with real government datasets, and honestly we learned just as much from the process as we did from the results. One of the biggest takeaways was how important it is to actually understand your data before writing any code. Both datasets needed careful inspection before we could even start cleaning. The FBI crime dataset in particular had a messy Excel structure with multi-row headers that caught us off guard. If we did this again we would spend a lot more time on exploratory data analysis before jumping into the merge and analysis steps.

We also learned that joining datasets from different sources is way more complicated than it sounds. The AQI dataset uses Core-Based Statistical Area names that represent entire metro regions, while the crime dataset uses individual city names. Trying to extract a city name from a CBSA string and match it to a city in the crime dataset introduced a lot of geographic imprecision that affected the quality of our final merged dataset. On top of that, version control habits really matter from day one. Early GitHub conflicts from inconsistent pulling and pushing slowed us down a lot and took extra time to sort out.

The biggest limitation of this project is that it lacks nuance. Both air quality and crime are heavily shaped by underlying factors like poverty, income inequality, population density, and unemployment. Without controlling for any of those variables, we cannot really say whether the relationship we observed between air quality and crime is a genuine environmental effect or just a reflection of the fact that economically disadvantaged areas tend to have both worse air quality and higher crime rates at the same time. Future work should bring in demographic data from the U.S. Census Bureau, things like median household income, poverty rate, and population density, to start untangling those confounding factors.

There are a few extensions that would make this analysis a lot stronger. First, instead of using the composite AQI score, future work could break air quality down by specific pollutant to see whether things like PM2.5 are more strongly tied to crime than others. Second, adding spatial analysis tools like geographic clustering or mapping would let us actually visualize where high-pollution and high-crime areas overlap and spot regional patterns that are hard to see in a table. A map visualization would also just make the findings a lot easier to communicate to someone outside of a data science context. Third, it would be interesting to look at whether specific types of crime are more associated with air quality than others. We only looked at violent and property crime as broad categories, but breaking those down into subcategories like assault, robbery, or burglary might reveal more specific patterns worth following up on.

Overall this project was a solid introduction to acquiring, cleaning, merging, and analyzing real-world government datasets. The findings are pretty basic but they do suggest that the relationship between environmental quality and public safety is worth exploring further with more detailed methods and better data. There is a lot of nuance in this topic and no single correlation is ever going to imply causation, so it is important to keep acknowledging all the other factors that are likely driving what we observed.

## Challenges

(We will write later)

## Reproducing

Here is your **fully integrated Reproducing section** (clean, consistent, and ready to paste into `README.md`):

---

## Reproducing

### 1. Clone the repository

```bash
git clone <repo-url>
cd IS477-Project
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Data acquisition

#### AQI dataset (automated download)

The AQI dataset is downloaded and extracted automatically using:

```bash
python3 download_data.py
```

Source:
[https://aqs.epa.gov/aqsweb/airdata/annual_aqi_by_cbsa_2024.zip](https://aqs.epa.gov/aqsweb/airdata/annual_aqi_by_cbsa_2024.zip)

This script downloads and prepares `annual_aqi_by_cbsa_2024.csv` for analysis.

---

#### Crime dataset (manual download)

The crime dataset was downloaded from the FBI Crime Data Explorer (CDE), available at [https://cde.ucr.cjis.gov](https://cde.ucr.cjis.gov). We accessed the “Crime in the United States Annual Reports” section and selected the 2024 release. The full dataset was downloaded as a compressed file. After extraction, we used the file *CIUS_Table_8_Offenses_Known_by_City_2024.xlsx*, which contains offense counts organized by state and city for 2024.

Because the FBI Crime Data Explorer does not provide a stable API or direct CSV endpoint, the dataset cannot be programmatically retrieved. For reproducibility, the raw file must be downloaded manually following the steps above. The data is then processed using `CrimeDataset.ipynb`, which performs cleaning and outputs the final file `crime_cleaned.csv` used in the pipeline.

---

### 4. Verify data integrity (SHA-256 checksums)

Run:

```bash
python3 verify_checksums.py --aqi annual_aqi_by_cbsa_2024.csv --crime crime_cleaned.csv
```

Expected checksums:

* AQI: `548c45b5b8822f5bcd988a17ea55726134ca668b82151c418ce3f7b3b2663cff`
* Crime: `9ede2384558c90fe0a5b22d68ae41d2449755d0d6de7dad64681ea0d297dd0b8`

Both files must pass verification before continuing.

---

### 5. Run full pipeline (recommended)

```bash
snakemake --cores 1
```

This executes the full workflow:

* AQI download and extraction
* checksum verification
* dataset merging
* analysis and visualization

---

### 6. Manual execution (optional)

If running step-by-step instead of Snakemake:

* `CrimeDataset.ipynb` → cleans crime dataset
* `EnvironmentDataset.ipynb` → explores AQI dataset
* `merge.py` → merges datasets into `merged_aqi_crime.csv`
* `analyze.py` → generates analysis outputs and visualizations

---

### Output files

After successful execution, the following files are generated:

* `annual_aqi_by_cbsa_2024.csv`
* `crime_cleaned.csv`
* `merged_aqi_crime.csv`
* `analysis_output.txt`
* Visualization PNG files

---

## References

Federal Bureau of Investigation. (2024). *Crime in the United States 2024: Offenses Known to Law Enforcement by State by City*. FBI Crime Data Explorer. https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/downloads

U.S. Environmental Protection Agency. (2024). *Annual Summary of Air Quality Index (AQI) Statistics by Core Based Statistical Area (CBSA), 2024*. Air Quality System Data Mart. https://aqs.epa.gov/aqsweb/airdata/download_files.html#Annual
