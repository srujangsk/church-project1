from natsort import natsorted  # Ensure you have the 'natsort' library installed

with open('titles_mod.txt', 'r', encoding='utf-8') as titles_file, open('links_mod.txt', 'r', encoding='utf-8') as links_file:
    titles = titles_file.readlines()
    links = links_file.readlines()

# Ensure both files have the same number of lines
if len(titles) != len(links):
    print("Error: Number of lines in titles_mod.txt and links_mod.txt should be the same.")
    exit()

# Extract only Telugu part of the titles, zip titles and links, then sort based on Telugu titles in alphabetical order
sorted_links = natsorted(zip([title.split('-')[0].strip() for title in titles], links), key=lambda x: x[0])

# Generate HTML code
html_code = "<html>\n<body>\n"

for title, link in sorted_links:
    title = title.strip()
    link = link.strip()
    html_code += f'<a href="{link}">{title}</a><br>\n'

html_code += "</body>\n</html>"

# Write HTML code to a file
with open('output.html', 'w', encoding='utf-8') as output_file:
    output_file.write(html_code)

print("HTML code generated and saved to output.html.")
