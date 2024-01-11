import os

def generate_html(input_folder, output_html_file_path):
    # Get all text files in the input folder
    text_files = [f for f in os.listdir(input_folder) if f.endswith(".txt")]

    # Sort text files based on their filenames
    text_files.sort()

    # Initialize HTML content
    html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Songs</title>
</head>
<body>
    <h1>List of Songs</h1>
'''

    # Loop through each text file and extract content
    for text_file in text_files:
        file_path = os.path.join(input_folder, text_file)

        # Extract title and lyrics from the text file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().split("||", 1)

            # Check if content has both title and lyrics
            if len(content) == 2:
                title = text_file[:-4].strip()  # Use filename without extension as the title
                lyrics = content[1].strip()

                # Replace newlines with <br> tags
                lyrics_html = '<br>'.join(lyrics.split('\n'))

                # Add song to HTML content
                html_content += f'    <div><h2>|| {title}</h2><p>{lyrics_html}</p></div>\n'

    # Close HTML content
    html_content += '''
</body>
</html>
'''

    # Write HTML content to the output file
    with open(output_html_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(html_content)

# Example usage
generate_html("songs", "songs.html")
