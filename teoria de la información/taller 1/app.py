from flask import Flask, render_template, request, jsonify
from huffman_utils import build_huffman_tree, generate_codes, encode, calculate_entropy, calculate_average_length, calculate_efficiency
from collections import Counter
from tkinter import messagebox, filedialog
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])

def encode_message():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'Texto vacío'}), 400

    root = build_huffman_tree(text)
    codebook = generate_codes(root)
    encoded_message = encode(text, codebook)
    frequency = Counter(text)
    total = len(text)

    entropy = calculate_entropy(frequency, total)
    avg_len = calculate_average_length(codebook, frequency, total)
    efficiency = calculate_efficiency(entropy, avg_len)

    return jsonify({
        'codebook': codebook,
        'encoded_message': encoded_message,
        'entropy': round(entropy, 4),
        'average_length': round(avg_len, 4),
        'efficiency': round(efficiency, 2)
    })
def save_file(self):
        if not self.codebook:
            messagebox.showwarning("Advertencia", "Primero codifique un mensaje.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Archivos JSON", "*.json")])
        if path:
            with open(path, 'w') as f:
                json.dump({
                    "codebook": self.codebook,
                    "encoded_message": self.encoded_message
                }, f, indent=4)
            messagebox.showinfo("Guardado", "Archivo guardado correctamente.")
if __name__ == '__main__':
    app.run(debug=True)
