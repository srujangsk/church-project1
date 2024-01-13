document.addEventListener('DOMContentLoaded', function () {
    const songList = document.getElementById('songList');
    const songDetails = document.getElementById('songDetails');

    fetch('/songs')
        .then(response => response.json())
        .then(songFiles => {
            // Display the list of songs.
            songFiles.forEach(songFile => {
                const listItem = document.createElement('li');
                listItem.textContent = songFile;
                listItem.addEventListener('click', () => showSongDetails(songFile));
                songList.appendChild(listItem);
            });
        })
        .catch(error => console.error('Error fetching song list:', error));

    function showSongDetails(songFile) {
        fetch(`/songs/${encodeURIComponent(songFile)}`)
            .then(response => response.text())
            .then(songLyrics => {
                const songDetailsContent = `<strong>${songFile}</strong><br />${songLyrics}`;
                songDetails.innerHTML = songDetailsContent;
            })
            .catch(error => console.error('Error fetching song details:', error));
    }
});
