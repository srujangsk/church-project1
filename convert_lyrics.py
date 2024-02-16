import os
import re

input_folder = "all_text_files"
output_folder = "vignapana_atmeeya_geethalu"
output_log_file = "conversion_log.txt"
song_color = "#ffffff"  # Text color (white in this case)
background_color = "#005580"  # Background color (a shade of blue in this case)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def clean_song_title(first_line):
    cleaned_title = re.sub(r'(?i)ప\s*:\s*| ప\s*:\s*| ప :\s*| ప\s*:\s*| ప: ', '', first_line)
    cleaned_title = cleaned_title.replace("ఆత్మీయ", "ఆత్మీయ")
    return cleaned_title

# Write the main content conversion logic
with open(output_log_file, "w") as log:
    for filename in os.listdir(input_folder):
        with open(os.path.join(input_folder, filename), "r", encoding="utf-8") as file:
            first_line = file.readline().strip()
            song_title = clean_song_title(first_line)

            output_filename = os.path.join(output_folder, f"{song_title}.html")

            with open(output_filename, "w") as output_file:
                output_file.write("<!DOCTYPE html>\n")
                output_file.write("<html>\n")
                output_file.write("<head>\n")
                output_file.write(f"<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
                output_file.write("<style>\n")
                output_file.write(f"body {{ font-size: 16px; color: {song_color}; background-color: {background_color}; }}\n")
                output_file.write("h1, h2 { text-align: center; }\n")
                output_file.write("img { max-width: 100%; height: auto; display: block; margin: 0 auto; }\n")
                output_file.write("</style>\n")
                output_file.write("</head>\n")
                output_file.write("<body>\n")
                output_file.write(f"<h1 style='color: {song_color}'>విజ్ఞాపన ఆత్మీయ గీతాలు</h1>\n")
                output_file.write(f"<h2>{song_title}</h2>\n")
                output_file.write("<br>\n")
                output_file.write(f"{first_line}<br>\n")
                for line in file:
                    output_file.write(f"{line.strip()}<br>\n")
                output_file.write("</body>\n")
                output_file.write("</html>")

            log.write(f"Converted {filename} to {output_filename}\n")

# Generate the index file with links including folder path and in alphabetical order
file_names = sorted(os.listdir(output_folder))
with open("index.html", "w") as index_file:
    index_file.write("<!DOCTYPE html>\n")
    index_file.write("<html>\n")
    index_file.write("<head>\n")
    index_file.write(f"<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
    index_file.write("</head>\n")
    index_file.write("<body style='color: white; background-color: #005580;'>\n")
    index_file.write(f"<h1 style='color: {song_color}'>విజ్ఞాపన ఆత్మీయ గీతాలు</h1>\n")
    index_file.write("<ul>")
    for filename in file_names:
        index_file.write(f'<li><a href="{os.path.join(output_folder, filename)}" style="color: {song_color}">{filename.replace(".html", "")}</a></li>')
    index_file.write("</ul>")
    index_file.write("</body>\n")
    index_file.write("</html>")

print("Conversion completed. Check log file for details.")
