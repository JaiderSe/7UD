import heapq
import math
import json
from collections import Counter
from tkinter import *
from tkinter import filedialog, messagebox

# Nodo para el árbol de Huffman
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Para que el heapq pueda ordenar los nodos
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = Counter(text)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, prefix="", codebook={}):
    if node is None:
        return
    if node.char is not None:
        codebook[node.char] = prefix
    generate_codes(node.left, prefix + "0", codebook)
    generate_codes(node.right, prefix + "1", codebook)
    return codebook

def encode(text, codebook):
    return ''.join(codebook[char] for char in text)

def calculate_entropy(frequency, total):
    return -sum((freq/total) * math.log2(freq/total) for freq in frequency.values())

def calculate_average_length(codebook, frequency, total):
    return sum((frequency[char]/total) * len(code) for char, code in codebook.items())

def calculate_efficiency(entropy, avg_length):
    return (entropy / avg_length) * 100 if avg_length != 0 else 0

class HuffmanApp:
    def __init__(self, master):
        self.master = master
        master.title("Codificador Huffman")

        self.label = Label(master, text="Ingrese un mensaje:")
        self.label.pack()

        self.text_entry = Text(master, height=5)
        self.text_entry.pack()

        self.encode_button = Button(master, text="Codificar", command=self.encode_message)
        self.encode_button.pack()

        self.result_label = Label(master, text="")
        self.result_label.pack()

        self.text_output = Text(master, height=20, width=70)
        self.text_output.pack()

        self.save_button = Button(master, text="Guardar archivo", command=self.save_file)
        self.save_button.pack()

        self.codebook = {}
        self.encoded_message = ""

    def encode_message(self):
        text = self.text_entry.get("1.0", END).strip()
        if not text:
            messagebox.showwarning("Advertencia", "Por favor ingrese un mensaje.")
            return

        root = build_huffman_tree(text)
        self.codebook = generate_codes(root)
        self.encoded_message = encode(text, self.codebook)

        frequency = Counter(text)
        total = len(text)

        entropy = calculate_entropy(frequency, total)
        avg_length = calculate_average_length(self.codebook, frequency, total)
        efficiency = calculate_efficiency(entropy, avg_length)

        output = "Símbolos y códigos Huffman:\n"
        for char, code in self.codebook.items():
            output += f"'{char}': {code}\n"

        output += f"\nMensaje codificado:\n{self.encoded_message}\n"
        output += f"\nEntropía: {entropy:.4f} bits\n"
        output += f"Largo medio: {avg_length:.4f} bits\n"
        output += f"Eficiencia: {efficiency:.2f}%\n"

        self.text_output.delete("1.0", END)
        self.text_output.insert(END, output)

    def save_file(self):
        if not self.codebook or not self.encoded_message:
            messagebox.showwarning("Advertencia", "Primero codifique un mensaje.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text", "*.txt")])

        if file_path:
            with open(file_path, 'w') as f:
                json.dump({
                    "Diccionario": self.codebook,
                    "Mensaje codificado": self.encoded_message
                }, f, indent=4)
            messagebox.showinfo("Éxito", "Archivo guardado correctamente.")

if __name__ == "__main__":
    root = Tk()
    app = HuffmanApp(root)
    root.mainloop()
