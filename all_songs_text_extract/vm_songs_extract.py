import requests
from bs4 import BeautifulSoup

def print_paragraphs(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        paragraphs = soup.find_all('p')  # You can replace 'p' with the appropriate tag for paragraphs

        if paragraphs:
            for paragraph in paragraphs:
                print(paragraph.get_text())
        else:
            print('No paragraphs found on the page.')

    else:
        print(f"Failed to fetch the site. Status code: {response.status_code}")

def process_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        print(f"\nProcessing URL: {url}")
        print_paragraphs(url)

if __name__ == '__main__':
    # Replace 'vm_songs_links.txt' with the actual path to your file containing URLs
    urls_file_path = 'vm_songs_links.txt'
    process_urls_from_file(urls_file_path)