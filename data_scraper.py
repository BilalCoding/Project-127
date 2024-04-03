from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars"

browser = webdriver.Chrome("C:/Users/bilal/Desktop/Coding Files/BYJU's/Projects/127/chrome-win64/chrome-win64/chrome.exe")
browser.get(START_URL)

time.sleep(10)

scraped_data = []

def scrape():
    soup = BeautifulSoup(browser.page_source, "html.parser")
    star_table = soup.find("table", attrs={"class", "wikitable sortable sticky-header jquery-tablesorter"})
    table_body = star_table.find("tbody")
    table_rows = table_body.find_all("tr")
    for row in table_rows:
        table_cols = row.find_all("td")
        temp_list = []
        for col_data in table_cols:
            data = col_data.text.strip()
            temp_list.append(data)
        scraped_data.append(temp_list)
    print(scraped_data)

scrape()

stars_data = []

for i in range(0,len(scraped_data)):
    
    Star_names = scraped_data[i][2]
    Distance = scraped_data[i][4]

    required_data = [Star_names, Distance]
    stars_data.append(required_data)

print(stars_data)


# Define Header
headers = ['Star_name','Distance']  

# Define pandas DataFrame   
star_df_1 = pd.DataFrame(stars_data, columns=headers)

#Convert to CSV
star_df_1.to_csv('scraped_data.csv',index=True, index_label="id")