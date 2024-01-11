import os
import requests
from bs4 import BeautifulSoup

def print_paragraphs(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        paragraphs = soup.find_all('p')

        if paragraphs:
            return '\n'.join(str(paragraph.prettify()) for paragraph in paragraphs)
        else:
            return 'No paragraphs found on the page.'

    else:
        return f"Failed to fetch the site. Status code: {response.status_code}"

def create_html_file(title, content):
    # Create an HTML file in the 'songs_html2/' directory with the corresponding title
    file_name = f"songs_html2/{title}.html"
    with open(file_name, 'w', encoding='utf-8') as output_file:
        # Write the HTML content to the file
        output_file.write(f"<!DOCTYPE html>\n<html>\n<head>\n<title>{title}</title>\n</head>\n<body>\n{content}\n</body>\n</html>")

    print(f"Created HTML file: {file_name}")

def process_links_and_titles(links_file, titles_file):
    with open(links_file, 'r') as links_file, open(titles_file, 'r') as titles_file:
        links = links_file.readlines()
        titles = titles_file.readlines()

    # Create a directory named 'songs_html2' if it doesn't exist
    output_directory = 'songs_html2'
    os.makedirs(output_directory, exist_ok=True)

    for link, title in zip(links, titles):
        link = link.strip()
        title = title.strip()

        print(f"\nProcessing Link: {link} with Title: {title}")

        paragraphs_text = print_paragraphs(link)

        # Create HTML file for each link with the corresponding title in 'songs_html2/' directory
        create_html_file(title, paragraphs_text)

if __name__ == '__main__':
    # Replace 'links.txt' and 'titles.txt' with the actual paths to your files
    links_file_path = 'links.txt'
    titles_file_path = 'titles.txt'

    process_links_and_titles(links_file_path, titles_file_path)
