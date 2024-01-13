document.addEventListener('DOMContentLoaded', function () {
    const songList = document.getElementById('songList');

    // Assuming the songs folder is in the same directory as the HTML file.
    const songsFolder = 'songs/';

    // Fetch the list of songs.
    fetch(`${songsFolder}`)
        .then(response => response.text())
        .then(html => {
            // Parse the HTML content to extract file names.
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, 'text/html');
            const files = Array.from(doc.querySelectorAll('a')).map(a => a.textContent);

            // Display the list of songs.
            files.forEach(songFile => {
                const listItem = document.createElement('li');
                listItem.textContent = songFile;
                songList.appendChild(listItem);
            });
        })
        .catch(error => console.error('Error fetching song list:', error));
});
