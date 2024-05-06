import heapq
from collections import defaultdict,Counter 
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.lef = None
        self.right = None
        
    def __lt__(self, other):
        return self.freq < other.freq
    
def build_huffman_tree(text):
    frequency = Counter(text)
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)
    return priority_queue[0]
def encode_huffman_tree(root, encoding_table, current_code=""):
    if root is None:
        return
    if root.char is not None:
        encoding_table[root.char] = current_code
        return
    encode_huffman_tree(root.left, encoding_table, current_code + "0")
    encode_huffman_tree(root.right, encoding_table, current_code + "1")
    
def huffman_encode(text):
    root = build_huffman_tree(text)
    encoding_table = {}
    encode_huffman_tree(root, encoding_table)
    encoded_text = "".join(encoding_table[char] for char in text)
    return encoded_text, encoding_table

def huffman_decode(encoded_text, encoding_table):
    reverse_encoding_table = {code: char for char, code in encoding_table.items()}
    current_code = ""
    decoded_text = ""
    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_encoding_table:
            decoded_text += reverse_encoding_table[current_code]
            current_code=""
    return decoded_text

text="Akanksha"
encoded_text,encoding_table = huffman_encode(text)
print()
for k in sorted(encoding_table):
    print(k,":",encoding_table[k])
print("encoded text :",encoded_text)
decoded_text = huffman_decode(encoded_text,encoding_table)
print("Decoded text:",decoded_text)
                              
