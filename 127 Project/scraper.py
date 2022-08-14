from email import header
from turtle import distance
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"


browser = webdriver.Ie("C:/Users/HP/Desktop/IEDriverServer.exe")
browser.get(START_URL)



scraped_data = []

def scrape():
    soup = BeautifulSoup(browser.page_source, "HTML.parser")
    bright_star_table = soup.find("table", attr={"class", "wikitable"})
    table_body = bright_star_table.find('tbody')
    table_rows = table_body.find_all('tr')
    temp_list= []
    for row in table_rows :
        table_cols = row.find_all('td')
        print(table_cols)
        for col_data in table_cols:
            data= col_data.text.strip()
            print(data)
            temp_list.append(data)
        scraped_data.append(temp_list)

stars_data = []

for i in range(0, len(scraped_data)):

    Star_name = scraped_data[i][1]
    Distance = scraped_data[i][3]
    Mass = scraped_data[i][5]
    Radius = scraped_data[i][6]
    Lum = scraped_data[i][7]

headers = ["Star_name", "Distance", "Mass", "Radius", "Lum"]

star_df_1 = pd.DataFrame(stars_data, columns=header)
star_df_1.to_csv('scraped_data.csv', index=True, index_label="id")