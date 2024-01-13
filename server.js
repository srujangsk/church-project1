const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const songsFolder = path.join(__dirname, 'songs');

app.get('/songs', (req, res) => {
  fs.readdir(songsFolder, (err, files) => {
    if (err) {
      console.error(err);
      res.status(500).send('Internal Server Error');
    } else {
      const songTitles = files.map(file => path.parse(file).name);
      res.json(songTitles);
    }
  });
});

app.use(express.static('public')); // Serve your HTML, CSS, and JS files from the 'public' folder.

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}`);
});
