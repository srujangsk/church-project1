def create_html_from_text(text_file, html_file):
    with open(text_file, 'r') as file:
        lyrics = file.readlines()

    with open(html_file, 'w') as file:
        file.write('<html>\n')
        file.write('<head><title>Song Lyrics</title></head>\n')
        file.write('<body style="line-height: 0.8;">\n')  # Adjust the line height here

        for line in lyrics:
            if line.strip() != "":
                file.write(f'<p>{line.strip()}</p>\n')
            else:
                file.write('<br>\n')

        file.write('</body>\n')
        file.write('</html>\n')

    print(f'HTML file "{html_file}" has been created.')

text_file = '61.txt'
html_file = 'song_lyrics.html'
create_html_from_text(text_file, html_file)
