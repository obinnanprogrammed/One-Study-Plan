import requests
from bs4 import BeautifulSoup

# The URL of the OpenStax page you want to scrape
url = 'https://openstax.org/books'  # Example: List of OpenStax books

# Send a GET request to fetch the page content
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Page fetched successfully!")
else:
    print("Failed to retrieve the page.")