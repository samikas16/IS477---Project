**1) Update on Each Task**
We finished setting up our GitHub and finalized our team. We also finalize our research questions, confirmed which datasets we were gonna use. We also downloaded the datasets and reviewed their documentation to understand the variables and structure. We also finished cleaning the datasets by handling missing values and outliers, and did some basic exploratory analysis. We also narrowed down the scope of our data to only data collected in 2024. Finally, we started identifying key trends and patterns in the dataset to guide our next steps in merging the two datasets.

Here are the links to our datasets:
https://aqs.epa.gov/aqsweb/airdata/download_files.html#Annual

https://catalog.data.gov/dataset/uniform-crime-reporting-ucr-program?utm_source=chatgpt.com


**2) Updated Timeline**

Week 4 (Current): Both datasets cleaned and explored

Week 5: Merge datasets and begin analysis (Both)

Week 6: Examine relationships between pollution and crime (Both)

Week 7: Write analysis section of report (Both)

Week 8: Final review, GitHub update, and submission (Both)
  
**3) Changes to Project and Progress**

Since submitting our initial project plan, our team has made several updates based on both our progress and feedback we received from Milestone 2. The most important change we made was narrowing our datasets to focus specifically on 2024 data. Originally, we had specified 2025, but after locating the FBI crime dataset, we confirmed that 2024 is the most recent year available. To keep our analysis consistent, we decided to use 2024 data for both the crime dataset and the EPA air quality dataset. This ensures that the two datasets reflect the same time period when we merge them later in the project.

We also made our crime dataset more specific. Rather than using a broad UCR dataset, we identified and downloaded Table 8 — Offenses Known to Law Enforcement by State by City, 2024, directly from the FBI Crime Data Explorer. This table contains city-level crime data including violent crime, property crime, murder, rape, robbery, aggravated assault, burglary, larceny-theft, motor vehicle theft, and arson across 8,986 cities in the United States. This level of specificity will allow us to conduct a more meaningful analysis when we merge it with the EPA air quality data.

Additionally, we changed some of our tasks in the project timeline to better reflect our progress. We have not had the opportunity to merge both datasets and begin analysis yet, so those are tasks we plan to complete within the next week. This will set us up for success in the final weeks of the project.

Based on feedback from Milestone 2, we also made sure to document the license and direct URLs for our datasets more clearly. Both datasets come from official U.S. government agencies (the FBI and the EPA) and are in the public domain, meaning they are freely available for public use without copyright restrictions. The direct URL for the crime dataset is https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/downloads, and the EPA air quality dataset can be accessed at https://www.epa.gov/outdoor-air-quality-data.

**4) Challenges or Problems**

Some challenges we ran into were issues with our GitHub and the datasets. For our github involved, push rejections caused by conflicts between the local branch and updates already present on GitHub, relating to the initial README file. This required resolving the issue by pulling changes from the main repository and rebasing before successfully pushing updates. Additionally, there were minor challenges with ensuring that files were properly staged, committed, and pushed in the correct order.

Both datasets required some cleaning and preprocessing before analysis could begin. There were missing values across several columns,and outliers that we which addressed through removal. 

All of these issues highlighted the importance of maintaining a consistent workflow, including regularly pulling the latest changes, committing with clear messages, and verifying that the correct branch was being used. Overall, resolving these problems improved understanding of version control practices and learning more about the data cleaning process.

**5) Contribution Summaries**

Sreeja Nallamala:
For this milestone, I was responsible for locating, downloading, and cleaning the FBI crime dataset. This involved loading the Excel file into a Jupyter notebook in VS Code, renaming columns, handling missing values, forward-filling state names, and converting numeric columns to the correct data types. I also calculated summary statistics to understand the distribution of crime across cities and states, and added per capita crime rate columns to prepare the data for fair comparisons across cities of different sizes. Beyond the technical work, I also addressed feedback from Milestone 2 by documenting the dataset license, format, and direct URL more clearly in the progress report. Additionally, I updated the project timeline to reflect our current progress and what remains to be completed in the coming weeks. All of my work, including the cleaned dataset saved as a CSV file and the analysis notebook, has been committed and pushed to our shared GitHub repository so that my individual contributions are visible through the commit history.

Samika Sripathi:

So far from the past milestone to the current one, I have been responsible for finding and downloading the AQI (Air Quality Index) dataset. To then clean the dataset and analyze it, I downloaded the dataset, then using pandas, I used the pd.read_csv function to further analyze the dataset. The dataset was actually very clean, and all the variables and corresponding values were the same. I couldn't fill any missing or null values that we needed to drop. I also couldn't find any outlier values that were concerning, so I didn't drop any values that way. I think I found some basic summary statistics about the dataset, like which cities had the best AQIs and which ones had the worst, what the average AQIs were, and what the most common AQIs were. But after that, I provided an update on each task that was completed, and I explained our challenged wiht github and dataset cleaning above. In the future I hope to build more detailed visualizations and deeper analyses for merging the datasets later on and answering our research questions.
