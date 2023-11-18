import requests 
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'
response = requests.get(url)

if response.status_code == 200:  # Check if the request was successful
    soup = BeautifulSoup(response.content, 'html.parser')

    book_items = soup.find_all("article", class_='product_pod')

    for book_item in book_items:
        title = book_item.h3.a["title"]
        # Handle the case where the rating might be missing
        rating_element = book_item.find('p', class_='star-rating')
        if rating_element:
            rating = rating_element['class'][1]
        else:
            rating = 'No rating available'

        print(f"Title: {title} , Rating: {rating}")
else:
    print("Failed to retrieve the page")

