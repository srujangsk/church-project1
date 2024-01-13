import os
import requests
from bs4 import BeautifulSoup

def extract_text(paragraph):
    return ' '.join(paragraph.stripped_strings)

def print_paragraphs(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        paragraphs = soup.find_all('p')  # You can replace 'p' with the appropriate tag for paragraphs

        if paragraphs:
            return '\n\n'.join(extract_text(paragraph) for paragraph in paragraphs)
        else:
            return 'No paragraphs found on the page.'

    else:
        return f"Failed to fetch the site. Status code: {response.status_code}"

def process_links_and_titles(links_file, titles_file):
    with open(links_file, 'r') as links_file, open(titles_file, 'r') as titles_file:
        links = links_file.readlines()
        titles = titles_file.readlines()

    # Create a directory named 'songs2' if it doesn't exist
    output_directory = 'songs2'
    os.makedirs(output_directory, exist_ok=True)

    for link, title in zip(links, titles):
        link = link.strip()
        title = title.strip()

        print(f"\nProcessing Link: {link} with Title: {title}")

        paragraphs_text = print_paragraphs(link)

        # Create a separate text file in the 'songs2/' directory for each link with the corresponding title
        file_name = f"{output_directory}/{title}.txt"
        with open(file_name, 'w', encoding='utf-8') as output_file:
            output_file.write(paragraphs_text)

        print(f"Created file: {file_name}")

if __name__ == '__main__':
    # Replace 'links.txt' and 'titles.txt' with the actual paths to your files
    links_file_path = 'links.txt'
    titles_file_path = 'titles.txt'
    
    process_links_and_titles(links_file_path, titles_file_path)
