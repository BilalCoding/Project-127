# Importing libraries
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests

# URL of brightest stars wikipage
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars"

# Halting the program for 10 seconds so that the web browser can load
time.sleep(10)

# Creating an empty list which will hold the data scraped from the wikipage
scraped_data = []

# Function to scrape the data from the wikipage
def scrape():
    # Sending a request to open the wikipage
    page = requests.get(START_URL)
    soup = BeautifulSoup(page.content, "html.parser")

    # Finding the tables and storing all the rows' data into table_rows
    tables = soup.find_all("table", attrs={"class", "wikitable"})
    star_table = tables[2]
    table_body = star_table.find("tbody")
    table_rows = table_body.find_all("tr")

    # Finding the column data in each row
    for row in table_rows:
        table_cols = row.find_all("td")
        # Creating a temporary list to store the column data of one row
        temp_list = []

        # Formatting the column data to be appended into the temp_list
        for col_data in table_cols:
            data = col_data.text.strip()
            temp_list.append(data)
        
        # Appending the column data of one row into the scraped_data list
        scraped_data.append(temp_list)

# Calling the scrape() function
scrape()

stars_data = []

for star in scraped_data:
    try:
        name = star[2]
    except:
        name = "NaN"
    try:
        distance = star[4]
    except:
        distance = "NaN"

    required_data = [name, distance]
    stars_data.append(required_data)

# Define Header
headers = ['Star_name','Distance']  

# Define pandas DataFrame   
star_df_1 = pd.DataFrame(stars_data, columns=headers)

#Convert to CSV
star_df_1.to_csv('scraped_data.csv',index=True, index_label="id")
