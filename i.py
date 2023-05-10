import heapq
from collections import defaultdict

def huffman_tree(frequency):
    heap = [[weight, [char, ""]] for char, weight in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return heap[0]

def huffman_codes(tree):
    huff_codes = {}
    for pair in tree[1:]:
        char, code = pair
        huff_codes[char] = code
    return huff_codes

def decompress(encoded_message, codes):
    inv_codes = {v: k for k, v in codes.items()}
    message = ""
    buffer = ""

    for bit in encoded_message:
        buffer += bit
        if buffer in inv_codes:
            message += inv_codes[buffer]
            buffer = ""

    return message

frequency = {
    'A': 11, 'B': 2, 'C': 4, 'D': 3, 'E': 14, 'G': 3, 'I': 6, 'L': 6, 'M': 3, 'N': 6,
    'O': 7, 'P': 4, 'Q': 1, 'R': 10, 'S': 4, 'T': 3, 'U': 4, 'V': 2, ' ': 17, ',': 2
}

tree = huffman_tree(frequency)
codes = huffman_codes(tree)

encoded_message1 = "1000101110101100001011101000111000001101100000011110011110100101100001101001110011010001011101011111110100001111001111110011110100011000110000001011010111101111111011101011011011100111011011110011111110010100101001010000101101011000101100110100011100100101100001100100011010110101011111111111011011101100110001000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100"
encoded_message2 = "0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010"

decompressed_message1 = decompress(encoded_message1, codes)
decompressed_message2 = decompress(encoded_message2, codes)

print("Decompressed message 1:", decompressed_message1)
print("Decompressed message 2:", decompressed_message2)
