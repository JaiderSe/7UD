import heapq
import math
from collections import Counter

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
