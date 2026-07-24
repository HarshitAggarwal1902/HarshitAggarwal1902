import requests
from bs4 import BeautifulSoup
import json
import os

GITHUB_USERNAME = "HarshitAggarwal1902"

def fetch_contributions(username):
    url = f"https://github.com/users/{username}/contributions"
    print(f"Fetching contributions from: {url}")
    
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch data: HTTP {response.status_code}")
        # Default empty data if it fails (e.g., if username is not set)
        return {"days": []}
        
    soup = BeautifulSoup(response.text, 'html.parser')
    
    days_data = []
    # Find all table cells that represent days
    for td in soup.find_all('td', class_='ContributionCalendar-day'):
        date = td.get('data-date')
        level_attr = td.get('data-level')
        if not date or level_attr is None:
            continue
            
        level = int(level_attr)
        days_data.append({
            "date": date,
            "level": level
        })
        
    return {"days": days_data}

if __name__ == "__main__":
    data = fetch_contributions(GITHUB_USERNAME)
    
    # Ensure data directory exists
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data")
    os.makedirs(data_dir, exist_ok=True)
    
    out_path = os.path.join(data_dir, "contributions.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"Saved {len(data['days'])} days of contributions to {out_path}")
