import requests
from bs4 import BeautifulSoup
import json

def get_ip_info(ip_address):
    """Fetch IP information from an online API."""
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    return response.json()

def scrape_website(url):
    """Scrape the title and meta description of a website."""
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string if soup.title else 'No title found'
        description = soup.find('meta', attrs={'name': 'description'})
        description_content = description['content'] if description else 'No description found'
        return title, description_content
    except Exception as e:
        return None, str(e)

def main():
    # Example IP address for demonstration
    ip_address = "8.8.8.8"
    ip_info = get_ip_info(ip_address)
    print(json.dumps(ip_info, indent=4))

    # Example website for demonstration
    url = "https://www.example.com"
    title, description = scrape_website(url)
    print(f"Title: {title}\nDescription: {description}")

if __name__ == "__main__":
    main()