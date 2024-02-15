import os

def lyrics_to_html(lyrics_file, html_file):
  """
  Converts song lyrics from a text file to an HTML file.

  Args:
    lyrics_file: Path to the text file containing song lyrics.
    html_file: Path to the desired output HTML file.
  """
  with open(lyrics_file, "r") as f:
    lyrics = f.read()

  # Add basic HTML structure
  html_content = f"<!DOCTYPE html><html><head><title>Song Lyrics</title></head><body>"

  # Split lyrics into lines and wrap in <p> tags
  for line in lyrics.splitlines():
    html_content += f"<p>{line}</p>"

  # Close HTML tags
  html_content += "</body></html>"

  # Write HTML content to the output file
  with open(html_file, "w") as f:
    f.write(html_content)

# Replace with your actual file paths
lyrics_file = "61.txt"
html_file = "song_lyrics.html"

lyrics_to_html(lyrics_file, html_file)

print(f"Converted lyrics from {lyrics_file} to {html_file}")
