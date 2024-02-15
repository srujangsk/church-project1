// app.js
const express = require('express');
const fs = require('fs');

const app = express();
const port = 3000;

app.get('/', (req, res) => {
    // Read the content of the file (sample.txt) in the current directory
    fs.readFile('sample.txt', 'utf8', (err, data) => {
        if (err) {
            return res.status(500).send('Error reading the file.');
        }

        // Display the content of the file in the response
        res.send(`<h1>File Content</h1><pre>${data}</pre>`);
    });
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});

