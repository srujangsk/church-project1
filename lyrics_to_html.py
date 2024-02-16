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
    
    # Extracting the song name without spaces and extra html extension
    #song_name = first_line.replace(" ", "")
    song_name = first_line
    if song_name.endswith(".html"):
        song_name = song_name[:-5]
    
    html_file_path = os.path.join("vignapana_atmeeeya_geethalu", f"{song_name}.html")
    
    with open(html_file_path, 'w') as file:
        file.write(f"<html><head><meta name='viewport' content='width=device-width, initial-scale=1.0'></head><body style='background-color: #F0F0F0'><h1>{main_heading}</h1><h2>{first_line}</h2><pre class='lyrics'>{lyrics}</pre></body></html>")
    
    log_file.write(f"{file_path} converted to {html_file_path}\n")
    
    return f"vignapana_atmeeeya_geethalu/{song_name}.html", first_line

def create_index_file(song_links):
    index_file_path = "index.html"
    with open(index_file_path, 'w') as file:
        file.write("<html><head><meta name='viewport' content='width=device-width, initial-scale=1.0'></head><body><h1>విజ్ఞాపన ఆత్మీయ గీతాలు</h1>")
        for link, song_name in song_links:
            # Replace spaces in the link name with %20 for correct URL encoding
            encoded_link = link.replace(" ", "%20")
            file.write(f"<p><a href='{encoded_link}' style='text-decoration: none;'>{song_name}</a></p>")
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
                song_link, song_name = create_html_file(file_path, lyrics, log_file, main_heading)
                song_links.append((song_link, song_name))
    
    create_index_file(song_links)
    log_file.close()

if __name__ == "__main__":
    main()
    main()
