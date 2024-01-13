document.addEventListener('DOMContentLoaded', function () {
    const songList = document.getElementById('songList');

    const songsFolder = 'songs/';

    // Fetch the list of songs.
    fetchSongs();

    function fetchSongs() {
        fetch(`${songsFolder}`, {
            headers: {
                'Content-Type': 'text/html; charset=utf-8'
            }
        })
            .then(response => response.text())
            .then(html => {
                // Parse the HTML content to extract file names.
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, 'text/html');
                const files = Array.from(doc.querySelectorAll('a')).map(a => a.textContent);

                // Display the list of songs.
                if (files.length > 0) {
                    files.forEach(songFile => {
                        const listItem = document.createElement('li');
                        listItem.textContent = songFile;
                        songList.appendChild(listItem);
                    });
                } else {
                    // Display a message if no files are found.
                    const listItem = document.createElement('li');
                    listItem.textContent = 'No songs found.';
                    songList.appendChild(listItem);
                }
            })
            .catch(error => console.error('Error fetching song list:', error));
    }
});
