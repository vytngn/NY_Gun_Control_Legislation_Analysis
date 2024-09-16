# NY Gun Control Legislation Analysis 
A data analysis project examining the relationship between New York gun control legislation coverage in The New York Times and gun violence incidents from 2014 to 2023. Utilizes the NYTimes API for data extraction and Python for processing, visualization, and insights.

# Summary

The purpose of this project was to investigate the relationship between New York gun control legislation coverage in The New York Times and the incidence of gun violence in New York over the past decade (from the beginning of 2014 to the end of 2023). Utilizing the NYTimes API, specific search parameters were defined to extract relevant article data. Python programming language and libraries such as requests, pickle, pandas, and pathlib were employed for data extraction, manipulation, and analysis. The analysis revealed yearly counts of articles on gun control legislation, offering significant insights into media coverage trends and their potential impact on gun violence incidents in New York during the specified period.

# Code Snippets 

1. **Setting up the API endpoint and key** 

  

   This code set up the API endpoint URL and the API key required for accessing the New York Time API. 

2. **Defining search parameters**

   

   - This snippet defines parameters for querying the New York Times API to retrieve relevant articles. It specifies search criteria such as the query `gun control`, filters for articles from the New York section, and narrows down by geographic location containing `"New York"` to include results from New York State. The date range from January 1, 2014, to December 31, 2023, ensures articles within a 10-year period. The initial page number for pagination is set to 0. This snippet is crucial for specifying criteria to retrieve relevant articles from The New York Times archive, essential for analyzing gun control legislation coverage over the specified period.

3. **Function to get total numbers of hits** 

   

   - `get_hits` retrieves the total number of articles (hits) related to a given query. It takes an optional parameter, query, which defaults to 'gun control' if not specified. By counting the volume of the articles, the function forms the basis for the data extraction phase.

4. **Function to get content for a specific page** 

   

   - The  function takes the `page_num` parameter, indicating the page number of search results, constructs the API request URL, sends a GET request, and parses the JSON response to extract the content of articles from the response. This function allows for efficient iteration through multiple pages of search results, enabling comprehensive data extraction. 

5. **Extracting and Storing Article Data**

   - This code snippet iterates through each article obtained from the API search results and extracts relevant information such as the publication year, headline, URL, and keywords. It then stores this information in a dictionary named `article_dict`. The publication year is extracted from the 'pub_date' field of the article and truncated to include only the year. The headline and URL are extracted from their respective fields in the article data. Keywords are extracted from the 'keywords' field, and a list of keywords is created and stored in the 'keyword' key of the `article_dict` dictionary.
   - This extracted data servers as raw input that will be stored in the subsequence phases of the ETL process. 

6. **Write Data to Pickle File**

   - This code snippet is crucial for saving the extracted article data into pickle files. 
   - Each pickle file contains the article data for a specific page of search results. 
   - The`pickle.dump()` function is used to serialize the `article_data` and write it to the pickle file. This process is essential for storing the extracted data locally.

   

7. **Extracting Keywords and Calculating Yearly Article Counts**![final.py (4)](/Users/avieng/Downloads/final.py (4).png)
   - This code snippet iterates through each article in the extracted data and checks if any of the keywords related to gun control legislation are present in the article. If such keywords are found, the article's URL is added to a set of unique URLs to avoid counting duplicate articles. Then, it checks if the publication year of the article matches any of the years in the `yearly_counts` dictionary. If a match is found, it increments the corresponding count in the `yearly_counts` dictionary.
   - This code snippet is essential for calculating the yearly counts of articles related to gun control legislation, which is crucial for understanding media coverage trends on this topic. These counts serve as a proxy for the level of public attention and discourse surrounding gun control legislation in New York over the specified period. By relating these counts to gun violence data, we can explore potential correlations or associations between media coverage and the incidence of gun violence.

8. **Saving Yearly Article Counts to CSV**![final.py (5)](/Users/avieng/Downloads/final.py (5).png)

- This code snippet saves the DataFrame containing yearly counts of articles related to gun control legislation into a CSV file named 'gun_control_legislation_counts.csv'. By doing so, it preserves the processed data for future reference, accessibility and analysis.



# Findings

According to Gun Violence Statistics from 2014 to 2024, reported by the Division of Criminal Justice Services, shooting incidents involving injury or death are considered gun violence in this case. These incidents represent instances where one or more individuals are injured or killed by a bullet, excluding non-criminal occurrences like accidental discharges or justifiable homicide. Analysis of the data reveals fluctuations in both media coverage of gun control legislation and the number of shooting incidents in New York over the last decade. 

Notably, there appears to be a correlation between peaks in shooting incidents and increased media attention on gun control legislation. For instance, the highest number of shooting incidents occurred in 2021, totaling 1262 incidents, which coincided with a notable increase in media coverage of gun control legislation that year. The year right after the most number of shooting incidents occurred, 2022, witnessed a peak in media coverage, with 59 articles related to gun control legislation. These findings suggest a potential relationship between heightened public concern and, government attention about gun violence and increased legislative discourse.



**Visualizations:** 

**Article Counts by Year through NYTimes API** 

*gun_control_legislation.csv*



**Visualization of the Article Counts** 





**Shooting Incidents of GIVE Shooting Activity Report from year 2014 to 2024**



# Conclusion

The results of the analysis meet my expectations, indicating a logical correlation between gun violence incidents and media coverage of gun control legislation, which suggests that public discourse may influence policy responses to gun violence. 

Moving forward, I would analyze trends and patterns in social media discussions about gun violence to capture a more comprehensive view of public discourse on gun violence and gun control. It would also be interesting to investigate the effectiveness of policy responses to gun violence and their impact on reducing incidents over time and on reducing public concerns. 

# References  

New York State Division of Criminal Justice Services. (2024, February 9). Gun Involved Violence Elimination (GIVE) Initiative: Annual GIVE Shooting Activity Report. Retrieved from [https://www.criminaljustice.ny.gov/crimnet/ojsa/GIVE%20Annual.pdf]
