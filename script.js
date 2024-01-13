document.addEventListener('DOMContentLoaded', function () {
    const songList = document.getElementById('songList');
    const songDetails = document.getElementById('songDetails');

    // Assuming your songs are directly inside the "songs" folder.
    const songsFolder = 'songs/';

    // Fetch the list of songs.
    fetchSongList();

    function fetchSongList() {
        // Simulate fetching the list of songs (replace with your logic).
        const songFiles = ['song1.txt', 'song2.txt', 'song3.txt']; // Replace with your actual file names.

        // Display the list of songs.
        songFiles.forEach(songFile => {
            const listItem = document.createElement('li');
            listItem.textContent = songFile.replace('.txt', ''); // Display the song name without the file extension.
            listItem.addEventListener('click', () => showSongDetails(songFile));
            songList.appendChild(listItem);
        });
    }

    function showSongDetails(songFile) {
        // Simulate fetching song details (replace with your logic).
        const songDetailsContent = `Song Title: ${songFile.replace('.txt', '')}<br /> 
                                    Artist: Your Artist<br /> 
                                    Album: Your Album`;

        songDetails.innerHTML = songDetailsContent;
    }
});
