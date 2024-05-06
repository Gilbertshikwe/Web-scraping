import requests
from bs4 import BeautifulSoup

# Send an HTTP request to the target website
url = "https://en.wikipedia.org/wiki/Website"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all heading elements
headings = soup.find_all(["h1", "h2", "h3"])

# Extract the text from the headings
for heading in headings:
    print(heading.text)
