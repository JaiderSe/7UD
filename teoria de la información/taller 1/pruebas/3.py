import heapq
import math
import json
from collections import Counter
from tkinter import *
from tkinter import ttk, messagebox, filedialog

# Algoritmo Huffman
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
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

def calculate_entropy(freq, total):
    return -sum((f/total) * math.log2(f/total) for f in freq.values())

def calculate_average_length(codebook, freq, total):
    return sum((freq[c]/total) * len(code) for c, code in codebook.items())

def calculate_efficiency(entropy, avg_len):
    return (entropy / avg_len) * 100 if avg_len > 0 else 0

# Interfaz estilo osciloscopio
class HuffmanApp:
    def __init__(self, master):
        self.master = master
        master.title("Codificador Huffman - Estilo Osciloscopio")
        master.configure(bg="black")

        style = ttk.Style()
        style.configure("Oscilo.TButton", background="black", foreground="#00FF00", font=("Courier", 10), borderwidth=2)
        style.configure("TLabel", background="black", foreground="#00FF00", font=("Courier", 12))
        style.configure("TEntry", fieldbackground="black", foreground="#00FF00")
        
        self.codebook = {}
        self.encoded_message = ""

        self.label = ttk.Label(master, text="Ingrese un mensaje:")
        self.label.pack(pady=5)

        self.text_entry = Text(master, height=5, bg="black", fg="#00FF00", insertbackground="#00FF00", font=("Courier", 10))
        self.text_entry.pack(padx=10, fill=X)

        self.encode_button = ttk.Button(master, text="Codificar", style="Oscilo.TButton", command=self.encode_message)
        self.encode_button.pack(pady=10)

        self.output_frame = Frame(master, bg="black")
        self.output_frame.pack(padx=10, pady=5, fill=BOTH, expand=True)

        self.scrollbar = Scrollbar(self.output_frame)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.text_output = Text(self.output_frame, height=20, width=80, bg="black", fg="#00FF00",
                                insertbackground="#00FF00", font=("Courier", 10), yscrollcommand=self.scrollbar.set)
        self.text_output.pack(fill=BOTH, expand=True)
        self.scrollbar.config(command=self.text_output.yview)

        self.save_button = ttk.Button(master, text="Guardar archivo", style="Oscilo.TButton", command=self.save_file)
        self.save_button.pack(pady=5)

    def encode_message(self):
        text = self.text_entry.get("1.0", END).strip()
        if not text:
            messagebox.showwarning("Advertencia", "Ingrese un mensaje.")
            return

        root = build_huffman_tree(text)
        self.codebook = generate_codes(root)
        self.encoded_message = encode(text, self.codebook)
        frequency = Counter(text)
        total = len(text)

        entropy = calculate_entropy(frequency, total)
        avg_len = calculate_average_length(self.codebook, frequency, total)
        efficiency = calculate_efficiency(entropy, avg_len)

        output = "Símbolos y códigos Huffman:\n"
        for char, code in sorted(self.codebook.items()):
            safe_char = char if char.isprintable() else f"\\x{ord(char):02x}"
            output += f"'{safe_char}': {code}\n"

        output += "\nMensaje codificado:\n" + self.encoded_message + "\n"
        output += f"\nEntropía: {entropy:.4f} bits\n"
        output += f"Largo medio: {avg_len:.4f} bits\n"
        output += f"Eficiencia: {efficiency:.2f}%\n"

        self.text_output.delete("1.0", END)
        self.text_output.insert(END, output)

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

if __name__ == "__main__":
    root = Tk()
    root.geometry("750x600")
    app = HuffmanApp(root)
    root.mainloop()
