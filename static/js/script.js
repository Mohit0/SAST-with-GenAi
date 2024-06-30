document.getElementById('fileInput').addEventListener('change', function(event) {
    const file = event.target.files[0];
    const previewContainer = document.getElementById('previewContainer');
    const previewImage = document.getElementById('previewImage');

    if (file) {
        const reader = new FileReader();
        
        reader.onload = function(e) {
            previewImage.src = e.target.result;
            previewContainer.style.display = 'block';
            
            setTimeout(() => {
                previewImage.style.opacity = 1;
            }, 1000); // 1-second delay for the transition
        };

        reader.readAsDataURL(file);
    }
});

document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Form submitted!');
});
