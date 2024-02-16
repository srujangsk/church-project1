import os
import re

def create_html_file(file_path, lyrics, log_file):
    first_line = lyrics.split("\n")[0].strip()
    match = re.search(r'(.*?)\s*(\(2\)|\|2\|\|\|2\|\|)\s*$', first_line)
    if match:
        first_line = match.group(1)
    match = re.match('ప\s*:\s*', first_line)
    if match:
        first_line = re.sub('ప\s*:\s*', '', first_line)
    
    html_file_path = f"vignapana_atmeeya_geethalu/{first_line}.html"

    with open(html_file_path, 'w') as file:
        file.write(f"<html><body><h2>{first_line}</h2><pre>{lyrics}</pre></body></html>")

    log_file.write(f"{file_path} converted to {html_file_path}\n")

def main():
    os.makedirs("vignapana_atmeeya_geethalu", exist_ok=True)

    log_file = open("output_log.txt", "w")
    lyrics_dir = "all_text_files"
    for file_path in os.listdir(lyrics_dir):
        if file_path.endswith(".txt"):
            with open(os.path.join(lyrics_dir, file_path), 'r') as file:
                lyrics = file.read()
                create_html_file(file_path, lyrics, log_file)

    log_file.close()

if __name__ == "__main__":
    main()
