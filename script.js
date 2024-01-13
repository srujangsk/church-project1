const songList = document.getElementById('song-list');
const songFolder = 'songs'; // The path to your song folder is already set here

const readSongs = () => {
    const songFiles = fs.readdirSync(songFolder);
    const songListHTML = songFiles.map(file => {
        const title = file.replace(/\.mp3$/i, ''); // Adjust for different file extensions if needed
        return `<li><a href="song.html?title=${title}">${title}</a></li>`;
    }).join('');
    songList.innerHTML = `<h2>Songs</h2><ul>${songListHTML}</ul>`;
};

// Check if the browser supports the File System Access API
if (typeof fs === 'undefined') {
    console.error('Browser does not support File System Access API.');
} else {
    readSongs();
}
