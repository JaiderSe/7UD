import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = Counter(text)
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    return heap[0]

def build_codes(node, prefix="", code_map=None):
    if code_map is None:
        code_map = {}
    if node:
        if node.char is not None:
            code_map[node.char] = prefix
        build_codes(node.left, prefix + "0", code_map)
        build_codes(node.right, prefix + "1", code_map)
    return code_map

def huffman_encode(text, code_map):
    return ''.join(code_map[char] for char in text)

def main():
    text = input("Ingresa el texto a cifrar: ")
    huffman_tree = build_huffman_tree(text)
    code_map = build_codes(huffman_tree)
    encoded_text = huffman_encode(text, code_map)

    print("\nTabla de códigos de Huffman:")
    for char, code in code_map.items():
        print(f"'{char}': {code}")
    print("\nTexto cifrado:")
    print(encoded_text)

if __name__ == "__main__":
    main()