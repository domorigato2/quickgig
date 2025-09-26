# scrape_gigs.py
import requests

app_id = "YOUR_APP_ID"  # Replace with Adzuna app_id
app_key = "YOUR_APP_KEY"  # Replace with Adzuna app_key
url = f"https://api.adzuna.com/v1/api/jobs/us/search/1?app_id={app_id}&app_key={app_key}&what=python&where=remote&results_per_page=5"
try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    jobs = data.get('results', [])
    with open('gigs.txt', 'w', encoding='utf-8') as f:
        for job in jobs:
            title = job.get('title', 'No title')
            company = job.get('company', {}).get('display_name', 'No company')
            f.write(f"{title} at {company}\n")
    print(f"Scraped {len(jobs)} gigs saved to gigs.txt")
except Exception as e:
    print(f"Error scraping: {e}")