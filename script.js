document.addEventListener('DOMContentLoaded', function () {
    const songList = document.getElementById('songList');
    const lyricsContainer = document.getElementById('lyricsContainer');
    const songsFolder = 'songs/';

    // Fetch the list of songs.
    fetchSongs();

    function fetchSongs() {
        // Simulate fetching the list of songs (replace with your logic).
        fetch(`${songsFolder}`)
            .then(response => response.json())
            .then(songFiles => {
                // Display the list of songs.
                songFiles.forEach(songFile => {
                    const listItem = document.createElement('li');
                    listItem.textContent = songFile.replace('.txt', '');
                    listItem.addEventListener('click', () => showLyrics(songFile));
                    songList.appendChild(listItem);
                });
            })
            .catch(error => console.error('Error fetching song list:', error));
    }

    function showLyrics(songFile) {
        // Simulate fetching song lyrics (replace with your logic).
        fetch(`${songsFolder}${songFile}`)
            .then(response => response.text())
            .then(lyrics => {
                lyricsContainer.innerHTML = `<h2>${songFile.replace('.txt', '')}</h2><p>${lyrics}</p>`;
            })
            .catch(error => console.error('Error fetching song lyrics:', error));
    }
});
