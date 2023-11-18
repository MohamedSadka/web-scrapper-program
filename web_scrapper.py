# planning the project
# find the website i want to scraper from
# finding the elements i want to choose from the site
# using modules like requests and beautifulsoup to pull the data from the site
# using the loop to get through all the data i want to extract
# print the data

import requests 
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

books = soup.find_all("article", class_='product_pod')

for book in books :
    title = book.h3.a["title"]
    rating = book.find('p', class_='star-rating')['class'][1]
    print(f"Title : {title} , Rating : {rating}")

