const fs = require('fs');
const path = require('path');

document.addEventListener('DOMContentLoaded', function () {
    const songList = document.getElementById('songList');
    const lyricsContainer = document.getElementById('lyricsContainer');
    const songsFolder = 'songs/';

    // Fetch the list of songs.
    const songFiles = fetchSongs();

    function fetchSongs() {
        // Simulate fetching the list of songs.
        try {
            const files = fs.readdirSync(songsFolder);
            return files.filter(file => path.extname(file) === '.txt');
        } catch (error) {
            console.error('Error fetching song list:', error);
            return [];
        }
    }

    // Display the list of songs.
    songFiles.forEach(songFile => {
        const listItem = document.createElement('li');
        listItem.textContent = songFile.replace('.txt', '');
        listItem.addEventListener('click', () => showLyrics(songFile));
        songList.appendChild(listItem);
    });

    function showLyrics(songFile) {
        // Simulate fetching song lyrics.
        try {
            const lyrics = fs.readFileSync(path.join(songsFolder, songFile), 'utf-8');
            lyricsContainer.innerHTML = `<h2>${songFile.replace('.txt', '')}</h2><p>${lyrics}</p>`;
        } catch (error) {
            console.error('Error fetching song lyrics:', error);
        }
    }
});
