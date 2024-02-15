import os
import requests
from bs4 import BeautifulSoup

def print_paragraphs(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        paragraphs = soup.find_all('p')  # You can replace 'p' with the appropriate tag for paragraphs

        if paragraphs:
            return '\n'.join(paragraph.get_text() for paragraph in paragraphs)
        else:
            return 'No paragraphs found on the page.'

    else:
        return f"Failed to fetch the site. Status code: {response.status_code}"

def create_html_file(title, content, output_directory):
    # Replace newline characters with HTML line break tags
    content_with_line_breaks = content.replace('\n', '<br>')

    # Create an HTML file in the specified output directory with the corresponding title
    file_name = os.path.join(output_directory, f"{title}.html")
    with open(file_name, 'w', encoding='utf-8') as output_file:
        # Write the HTML content to the file
        output_file.write(f"<!DOCTYPE html>\n<html>\n<head>\n<title>{title}</title>\n</head>\n<body>\n{content_with_line_breaks}\n</body>\n</html>")

    print(f"Created HTML file: {file_name}")

def process_links_and_titles(links_file, titles_file, output_directory):
    with open(links_file, 'r') as links_file, open(titles_file, 'r') as titles_file:
        links = links_file.readlines()
        titles = titles_file.readlines()

    # Create the specified output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    for link, title in zip(links, titles):
        link = link.strip()
        title = title.strip()

        print(f"\nProcessing Link: {link} with Title: {title}")

        paragraphs_text = print_paragraphs(link)

        # Create HTML file for each link with the corresponding title in the specified output directory
        create_html_file(title, paragraphs_text, output_directory)

if __name__ == '__main__':
    # Replace 'links.txt' and 'titles.txt' with the actual paths to your files
    links_file_path = 'links.txt'
    titles_file_path = 'titles.txt'
    
    # Specify the output directory for the new HTML files
    output_directory_path = 'songs_html2'
    
    process_links_and_titles(links_file_path, titles_file_path, output_directory_path)
