# scrape_gigs.py
import requests
from bs4 import BeautifulSoup

url = "https://www.indeed.com/jobs?q=python&l=remote"  # Python jobs, remote
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/117.0.0.0"
}
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = soup.find_all('h2', class_='jobTitle')
    with open('gigs.txt', 'w', encoding='utf-8') as f:
        for job in jobs:
            title = job.text.strip()
            f.write(title + '\n')
    print(f"Scraped {len(jobs)} gigs saved to gigs.txt")
except Exception as e:
    print(f"Error scraping: {e}")