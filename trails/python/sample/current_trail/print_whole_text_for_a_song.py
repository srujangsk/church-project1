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

if __name__ == '__main__':
    # Replace the URL with your actual link
    url = 'https://sites.google.com/view/vignapana-ministries-songs/%E0%B0%B5%E0%B0%9C%E0%B0%9E%E0%B0%AA%E0%B0%A8-%E0%B0%95%E0%B0%B0%E0%B0%A4%E0%B0%A8%E0%B0%B2/1-%E0%B0%A8-%E0%B0%B8%E0%B0%A8%E0%B0%A8%E0%B0%A6-%E0%B0%A8-%E0%B0%A4%E0%B0%A1%E0%B0%97-nee-sannidhe-naa-toduga'
    print_paragraphs(url)
