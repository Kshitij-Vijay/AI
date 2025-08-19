import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url: str) -> str:
    """Scrape text content from a Wikipedia page."""
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch {url}, status {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    text = "\n".join(p.get_text() for p in paragraphs)
    return text.strip()
