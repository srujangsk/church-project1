import requests
from bs4 import BeautifulSoup

# Replace with your Google Site URL
#url = "https://your-google-site.com"
url = "https://sites.google.com/view/vignapana-ministries-songs/%E0%B0%B5%E0%B0%9C%E0%B0%9E%E0%B0%AA%E0%B0%A8-%E0%B0%95%E0%B0%B0%E0%B0%A4%E0%B0%A8%E0%B0%B2/2-%E0%B0%A4%E0%B0%B0%E0%B0%B2-%E0%B0%AE%E0%B0%B0%E0%B0%A8-taralu-marina"

# Get the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find all <a> tags containing page links
links = soup.find_all("a", href=True)

# Extract and print the link URLs
for link in links:
    print(link["href"])
