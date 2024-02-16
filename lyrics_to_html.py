import os
import re

def create_html_file(file_path, lyrics, log_file, main_heading):
    first_line = lyrics.split("\n")[0].strip()
    match = re.search(r'(.*?)\s*(\(2\)|\|2\|\|\|2\|\|)\s*$', first_line)
    if match:
        first_line = match.group(1)
    match = re.match('ప\s*:\s*', first_line)
    if match:
        first_line = re.sub('ప\s*:\s*', '', first_line)
    
    html_file_path = os.path.join("vignapana_atmeeeya_geethalu", f"{first_line}.html")
    song_name = first_line.replace(" ", "").replace(".html", "")
    
    with open(html_file_path, 'w') as file:
        file.write(f"<html><head><meta name='viewport' content='width=device-width, initial-scale=1.0'></head><body style='background-color: #F0F0F0'><h1>{main_heading}</h1><h2>{first_line}</h2><pre class='lyrics'>{lyrics}</pre></body></html>")
    
    log_file.write(f"{file_path} converted to {html_file_path}\n")
    
    return f"vignapana_atmeeeya_geethalu/{song_name}.html"

def create_index_file(song_links):
    index_file_path = "index.html"    
    song_links.sort()  
    with open(index_file_path, 'w') as file:
        file.write("<html><head><meta name='viewport' content='width=device-width, initial-scale=1.0'></head><body><h1>విజ్ఞాపన ఆత్మీయ గీతాలు</h1>")
        for link in song_links:
            song_heading = link.split('/')[-1].split('.')[0]  
            file.write(f"<p><a href='{link}' style='text-decoration: none;'>{song_heading}</a></p>")
        file.write("</body></html>")

def main():
    os.makedirs("vignapana_atmeeeya_geethalu", exist_ok=True)
    log_file = open("output_log.txt", "w")
    lyrics_dir = "all_text_files"
    song_links = []
    
    main_heading = "విజ్ఞాపన ఆత్మీయ గీతాలు"
    
    for file_path in os.listdir(lyrics_dir):
        if file_path.endswith(".txt"):
            with open(os.path.join(lyrics_dir, file_path), 'r') as file:
                lyrics = file.read()
                song_link = create_html_file(file_path, lyrics, log_file, main_heading)
                song_links.append(song_link)
    
    created_song_links = [f"{link}.html" for link in song_links]
    create_index_file(created_song_links)
    log_file.close()

if __name__ == "__main__":
    main()
