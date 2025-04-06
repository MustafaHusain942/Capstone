// Image preview
document.getElementById('imageUpload').addEventListener('change', function(e) {
    const preview = document.getElementById('preview');
    const previewImage = document.getElementById('previewImage');
    const file = e.target.files[0];
    
    if (file) {
        previewImage.src = URL.createObjectURL(file);
        preview.classList.remove('hidden');
    }
});

// Form submission
document.getElementById('uploadForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const formData = new FormData();
    const fileInput = document.getElementById('imageUpload');
    formData.append('file', fileInput.files[0]);

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();
        
        if (data.error) {
            alert(data.error);
            return;
        }

        document.getElementById('prediction').textContent = data.prediction;
        document.getElementById('confidence').textContent = `${(data.confidence * 100).toFixed(2)}%`;
        document.getElementById('result').classList.remove('hidden');
    } catch (error) {
        alert('Error occurred during prediction');
        console.error(error);
    }
}); 