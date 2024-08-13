import requests
from bs4 import BeautifulSoup

def scrape_linkedin_profile(url):
    headers = {
        "User-Agent": "Your User Agent"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.context, 'html.parser')

    # Extract the name, title and company
    name = soup.find('li', {'class': 'inline t-24 t-block t-normal break-words'}).get_text(strip=True)
    title = soup.find('h2', {'class': 'mt1 t-18 t-black t-normal'}).get_text(strip=True)
    company = soup.find('h2', {'class': 't-16 t-black t-bold'}).get_text(strip=True)