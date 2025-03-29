import requests
from bs4 import BeautifulSoup

subject_books = {}

# The URL of the OpenStax page you want to scrape
url = 'https://openstax.org/subjects'  # Example: List of OpenStax books

# Send a GET request to fetch the page content
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Page fetched successfully!")
else:
    print("Failed to retrieve the page.")


# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# book_titles = soup.find_all('h3', class_='book-title')
subject_links = soup.find_all('a', href=True, tabindex='0')

# Extract subject names and URLs
subjects = []
for link in subject_links:
    # Extract the subject name (the text inside the <a> tag)
    subject_name = link.get_text().strip()
    
    # Extract the relative URL (the href value)
    subject_url = link['href']
    
    # Store the subject name and URL in a tuple or list
    subjects.append((subject_name, subject_url))

# Print out the subjects and their URLs
for subject, url in subjects:
    print(f"Subject: {subject}, URL: {url}")
