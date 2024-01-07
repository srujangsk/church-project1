# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Get started with interactive Python!
# Supports Python Modules: builtins, math,pandas, scipy 
# matplotlib.pyplot, numpy, operator, processing, pygal, random, 
# re, string, time, turtle, urllib.request
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp

import requests
from bs4 import BeautifulSoup

# Replace with your Google Site URL
url = "https://your-google-site.com"
url = "https://sites.google.com/view/vignapana-ministries-songs/%E0%B0%B5%E0%B0%9C%E0%B0%9E%E0%B0%AA%E0%B0%A8-%E0%B0%95%E0%B0%B0%E0%B0%A4%E0%B0%A8%E0%B0%B2"

# Get the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find all <a> tags containing page links
links = soup.find_all("a", href=True)

# Extract and print the link URLs
for link in links:
  #link = "https://sites.google.com/" + link["href"]
  print("https://sites.google.com", end="")
  print(link["href"])
