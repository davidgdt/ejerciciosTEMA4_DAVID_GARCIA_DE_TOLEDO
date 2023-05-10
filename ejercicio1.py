import heapq

class Node:
    def __init__(self, freq, char=None):
        self.freq = freq
        self.char = char
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def calculate_frequencies(character_count):
    total_count = sum(character_count.values())
    return {char: count / total_count for char, count in character_count.items()}

def build_huffman_tree(frequencies):
    heap = [Node(freq, char) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        parent = Node(left.freq + right.freq)
        parent.left = left
        parent.right = right

        heapq.heappush(heap, parent)

    return heap[0]

def generate_huffman_codes(tree, prefix=""):
    if tree is None:
        return {}

    if tree.char is not None:
        return {tree.char: prefix}

    left_codes = generate_huffman_codes(tree.left, prefix + "0")
    right_codes = generate_huffman_codes(tree.right, prefix + "1")

    return {**left_codes, **right_codes}

def decompress_huffman(message, huffman_tree, huffman_codes):
    result = []
    code = ""

    for bit in message:
        code += bit

        if code in huffman_codes.values():
            char = [k for k, v in huffman_codes.items() if v == code][0]
            result.append(char)
            code = ""

    return "".join(result)
character_count = {
    'A': 11, 'B': 2, 'C': 4, 'D': 3, 'E': 14, 'G': 3,
    'I': 6, 'L': 6, 'M': 3, 'N': 6, 'O': 7, 'P': 4,
    'Q': 1, 'R': 10, 'S': 4, 'T': 3, 'U': 4, 'V': 2,
    ' ': 17, ',': 2
}

frequencies = calculate_frequencies(character_count)
huffman_tree = build_huffman_tree(frequencies)
huffman_codes = generate_huffman_codes(huffman_tree)

message1 = "10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111111011101011011011100111011011110011111110010100101001010000010110101100010110011010001110010010110000110010001101011010101111111111101101111011100100001001010110001111111000100011101100110010110100011011111101011010001101110000000111001001010100011111100011001011010111001100111101000110001100000001011010111110011100"

message2 = "011010101101110010100011110101110011011101011011010000100011101010010111101001111111011100101000111101011100110111010110000110001001101000111001001000110001011001100111001001000011110111010010111011110001111101100110010110100011011111101011010001101110000000111001001010100011111100011001011010111001100111101000110001100000001011010111110011110110111011100111011011110011111110010100101001010000010110101100010110011010001110010010110000110001000110101101010111111111110110111101110010000100101011000111111100010001110110011001011010001101111110101101000110111000000011100100101010001111110001100101101011100110011110100011101000110000000101101011111001110110111011100111011011110011111110010100101001010000010110101100010110011010001110010010110000110001000110101101010111111111110110111101110010000100101011000111111100010001110110011001011010001101111110101101000110111000000011100100101010001111110001100101101011100110011110100011101000110000000101101011111001110"

decompressed_message1 = decompress_huffman(message1, huffman_tree, huffman_codes)
decompressed_message2 = decompress_huffman(message2, huffman_tree, huffman_codes)

print("Decompressed message 1:", decompressed_message1)
print("Decompressed message 2:", decompressed_message2)
