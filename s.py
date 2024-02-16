import os

# Define the folder containing the songs
folder_path = "vignapana_atmeeeya_geethalu"

# Get a list of all the song files in the folder
song_files = sorted(os.listdir(folder_path))

# Create the index.html file
with open("index.html", "w", encoding="utf-8") as file:
    file.write("<!DOCTYPE html>\n")
    file.write("<html>\n")
    file.write("<head>\n")
    file.write("<title>విజ్ఞాపన ఆత్మీయ గీతాలు</title>\n")
    file.write("</head>\n")
    file.write("<body>\n")
    file.write("<h1>విజ్ఞాపన ఆత్మీయ గీతాలు</h1>\n")
    file.write("<ul>\n")
    
    # Add links for each song in alphabetical order
    for song_file in song_files:
        song_name = os.path.splitext(song_file)[0]
        # Replace spaces with %20 in the URL encoding
        encoded_song_name = song_file.replace(" ", "%20")
        file.write(f"<li><a href=\"{folder_path}/{encoded_song_name}\">{song_name}</a></li>\n")
    
    file.write("</ul>\n")
    file.write("</body>\n")
    file.write("</html>")
    
print("index.html file has been created successfully.")
