import requests
from bs4 import BeautifulSoup
import csv
import time

BASE_URL = "http://quotes.toscrape.com/page/{}/"

def scrape_page(page_num):
    url = BASE_URL.format(page_num)
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to load page {page_num}")
        return None
    
    soup = BeautifulSoup(response.text, "html.parser")
    quotes_data = []

    # Grab all quotes on the page
    quotes = soup.find_all("div", class_="quote")

    for q in quotes:
        text = q.find("span", class_="text").get_text(strip=True)
        author = q.find("small", class_="author").get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in q.find_all("a", class_="tag")]
        
        quotes_data.append({
            "Quote": text,
            "Author": author,
            "Tags": ", ".join(tags)
        })
    
    return quotes_data

def main():
    all_quotes = []
    
    # Loop through first 10 pages
    for page in range(1, 11): 
        print(f"Scraping page {page}...")
        data = scrape_page(page)
        if not data:
            break
        all_quotes.extend(data)
        time.sleep(1)  # politeness delay
    
    # Save to CSV
    with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Quote", "Author", "Tags"])
        writer.writeheader()
        writer.writerows(all_quotes)
    
    print("Scraping done. Data saved to quotes.csv ✅")

if __name__ == "__main__":
    main()
