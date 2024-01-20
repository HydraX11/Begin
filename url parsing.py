from urllib.parse import urlparse, urljoin
import requests
from bs4 import BeautifulSoup


def get_all_paths(base_url):
    parsed_url = urlparse(base_url)

    scheme = parsed_url.scheme
    netloc = parsed_url.netloc
    unique_paths = set()
    session = requests.Session()
    def get_links_from_page(url):
        try:
            response = session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = [link.get('href') for link in soup.find_all('a')]
            return links
        except Exception as e:
            print(f"Error retrieving links from {url}: {e}")
            return []

    def extract_paths(url):
        #print("Requesting:", url)

        if url not in unique_paths:
            print("Requesting:", url)
            unique_paths.add(url)

            try:
                response = session.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                links = [link.get('href') for link in soup.find_all('a')]
                for link in links:
                    absolute_link = urljoin(base_url, link)
                    extract_paths(absolute_link)

            except Exception as e:
                print(f"Error retrieving links from {url}: {e}")

    extract_paths(base_url)
    return unique_paths

base_url = input("Enter the url which includes(https:// or http://): ")
result = get_all_paths(base_url)

print("\nPaths under", base_url)
for path in result:
    print(path)
