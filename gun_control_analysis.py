from math import ceil
from time import sleep
import pickle
import requests, pprint, csv, pathlib
import pandas as pd
import pathlib

''' ETL Process:
    1. Extract: Get the data from the API and store it in a list of dictionaries
    2. Transform: Convert the list of dictionaries to a pandas DataFrame and save it to a CSV file
    3. Load: Loop through each keyword file in the directory, 
        # extract the movie names, 
        # count the total hits for each movie, 
        # and save the results to a CSV file '''

# 1. Set up API end point and API key
url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
API_KEY = ''

# 2. Define search parameters for gun control legislation articles 
params = {
    'api-key': API_KEY,
    'q': 'gun control',
    'fq': 'section_name: ("New York") AND subject: ("Gun Control") glocations.contains: ("New York")',
    'document-type': 'article',
    'begin_date': '20140101',
    'end_date': '20231231',
    'page':0
    }

# 3. Function to get the total number of hits for a query 
def get_hits(query='gun control'):
    params['q'] = query
    content = requests.get(url, params=params).json()
    return content['response']['meta']['hits'] #return number of hit 

# 4. Function to get the content for a specific page 
def get_content(page_num):
    params['page'] = page_num
    content = requests.get(url, params=params).json()
    return content['response']['docs']

# 5. Initialize directory for storing data 
keyword_dir = pathlib.Path().cwd()/ 'keyword_dir'
keyword_dir.mkdir(exist_ok=True)

# 6. Variable field to hold article's data
hit_count = get_hits() # total number of hits for the query
page_count =  ceil(hit_count/10) #total number of page of query result
article_data = [] #empty list to store the article data


# STEP 2: LOAD DATA ----------------
# Loop through each page of the results
""" for page in range(page_count):
    # Get the content for the current page
    for article in get_content(0):
        # Initialize an empty dictionary to store the article data
        article_dict = {}
        # Add the headline, url, publish_date and keywords to the dictionary 
        '''{'headline': value,
            'url': value,
            'keyword': value 
            }'''
        article_dict['headline'] = article['headline']['main']
        article_dict['url'] = article['web_url']
        article_dict['keyword'] = article['keywords']
        article_dict['publish_year'] = article['pub_date'][:4] #extract the year of the data
        # Add the dictionary to the article data list
        article_data.append(article_dict)
        sleep(2)
print(article_data) """
""" # 7. Loop through pages and save article data into pickle docs
for page in range(page_count):
    article_info = [] # store article info  for this page 
    for article in get_content(page):
        article_dict = {}
        article_dict['publish_year'] = (article['pub_date'])[:4]
        article_dict['headline'] = article['headline']['main']
        article_dict['url'] = article['web_url']

        keyword_list = [] #empty list to store keyword
        for item in article['keywords']:
            keyword_list.append(item['value'])
        article_dict['keyword'] = keyword_list

        article_info.append(article_dict)

        file_name = f"article_info_{page}.pkl"
        file_path = keyword_dir/file_name
        with file_path.open(mode='wb') as file:
            pickle.dump(article_info, file)
        sleep(4) """


yearly_counts = {year: 0 for year in range(2014,2024)} #store yearly article counts 

# Count increment only if the publish year is in 2014 to 2023 and if the url is not already exist (avoid duplications)

tracked_urls = set()
# Loop through each pickle file in the article dir 
for file in keyword_dir.iterdir(): 
    with file.open(mode='rb') as file:
        article_info = pickle.load(file)
   
    # Loop through each article in the loaded data 
    for article_dict in article_info:
        for keyword in article_dict['keyword']:
            if 'gun control' in keyword.lower() or 'legislation' in keyword.lower() or 'legislature' in keyword.lower():
                if article_dict['url'] not in tracked_urls:
                    print(article_dict['headline'])
                    tracked_urls.add(article_dict['url'])
                # Check if the publish year of the article matches any of the years
                    for year,article_count in yearly_counts.items():
                        if int(article_dict['publish_year']) == year:
                            # Increment the count for the corresponding year
                            yearly_counts[year] += 1
            

#convert yearly_counts dictionary to list of typles 
yearly_counts_list = list(yearly_counts.items())

# 9. Convert yearly_counts dictionary to DataFrame 
yearly_counts_df = pd.DataFrame(yearly_counts_list, columns=['Year', 'Article_Count'])

# 10. Specify the file path for the CSV file
csv_file_path = 'gun_control_legislation_counts.csv'

# 11. Save the DataFrame to a CSV file 
yearly_counts_df.to_csv(csv_file_path, index=False)


