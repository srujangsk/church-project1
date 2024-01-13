def generate_html(links_file, titles_file, output_file):
    with open(links_file, 'r', encoding='utf-8') as links_file:
        links = links_file.readlines()

    with open(titles_file, 'r', encoding='utf-8') as titles_file:
        titles = titles_file.readlines()

    # Ensure the number of links and titles match
    if len(links) != len(titles):
        print("Error: Number of links and titles don't match.")
        return

    # Create HTML content
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Vignapana Ministries Songs</title>
        <script>
            function toggleOrder() {
                var list = document.getElementById("songList");
                var items = list.getElementsByTagName("li");
                var arr = [];

                for (var i = 0; i < items.length; i++) {
                    arr.push(items[i]);
                }

                arr.sort(function(a, b) {
                    var titleA = a.textContent.trim().replace(/^\d+\.\s/, '');  // Remove serial numbers
                    var titleB = b.textContent.trim().replace(/^\d+\.\s/, '');

                    // Sort based on Telugu letters
                    return titleA.localeCompare(titleB, 'en', { sensitivity: 'base' });
                });

                if (list.dataset.order === "original") {
                    for (var i = 0; i < arr.length; i++) {
                        list.appendChild(arr[i]);
                    }
                    list.dataset.order = "alphabetical";
                } else {
                    for (var i = 0; i < arr.length; i++) {
                        list.appendChild(items[i]);
                    }
                    list.dataset.order = "original";
                }
            }
        </script>
    </head>
    <body>

    <h1>Vignapana Ministries Songs</h1>

    <button onclick="toggleOrder()">Toggle Order</button>

    <ul id="songList">
    """

    songs = list(zip(titles, links))

    # Sort based on Telugu letters
    songs.sort(key=lambda x: x[0].strip())

    for title, link in songs:
        title_text = title.strip()  # Remove leading/trailing whitespaces
        html_content += f'        <li>{title_text}<a href="{link.strip()}">{title_text}</a></li>\n'

    html_content += """
    </ul>

    </body>
    </html>
    """

    # Write HTML content to the output file
    with open(output_file, 'w', encoding='utf-8') as output_file:
        output_file.write(html_content)

    print(f"HTML file '{output_file}' generated successfully.")

# Provide the file names
links_file_path = 'links.txt'
titles_file_path = 'titles.txt'
output_html_file_path = 'vignapana_songs.html'

# Generate HTML file
generate_html(links_file_path, titles_file_path, output_html_file_path)
