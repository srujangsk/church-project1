document.getElementById('fileInput').addEventListener('change', handleFileSelect);

function handleFileSelect(event) {
    const files = event.target.files;

    if (files.length === 0) {
        console.log('No files selected.');
        return;
    }

    console.log('Selected files:');

    for (let i = 0; i < files.length; i++) {
        const file = files[i];
        console.log(`${file.name} (type: ${file.type,} size: ${file.size} bytes)`);
    }
}
