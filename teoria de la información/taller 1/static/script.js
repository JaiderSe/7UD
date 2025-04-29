function encodeMessage() {
    const text = document.getElementById('inputText').value;

    fetch('/encode', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            const output = document.getElementById('output');
            output.innerHTML = `
                <h2>Resultados:</h2>
                <strong>Mensaje codificado:</strong> ${data.encoded_message}<br><br>
                <strong>Entropía:</strong> ${data.entropy} bits<br>
                <strong>Largo medio:</strong> ${data.average_length} bits<br>
                <strong>Eficiencia:</strong> ${data.efficiency}%<br><br>
                <strong>Diccionario Huffman:</strong><br>${JSON.stringify(data.codebook, null, 2)}
            `;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Function to encode the input text using Huffman coding
