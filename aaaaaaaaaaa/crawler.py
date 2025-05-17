import requests
from bs4 import BeautifulSoup
import re

base_url = "http://localhost:8080/.hidden/"

def crawl(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    for link in soup.find_all("a"):
        href = link.get("href")
        if href == "../":
            continue
        
        full_url = url + href
        if href.endswith("/"):
            crawl(full_url)
        else:
            file_response = requests.get(full_url)
            if "flag" in file_response.text:
                print(f"Found in {full_url}:")
                print(file_response.text)

crawl(base_url)
