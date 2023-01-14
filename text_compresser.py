import heapq
from collections import Counter, defaultdict

def compress_text(text):
    # Create a frequency table of the characters in the text
    freq_table = Counter(text)

    # Create a priority queue of the characters, sorted by frequency
    priority_queue = [[weight, [char, ""]] for char, weight in freq_table.items()]
    heapq.heapify(priority_queue)

    # Merge the lowest frequency characters until only one element remains in the queue
    while len(priority_queue) > 1:
        lo = heapq.heappop(priority_queue)
        hi = heapq.heappop(priority_queue)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(priority_queue, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    # Create a dictionary to store the Huffman codes for each character
    huffman_codes = dict(priority_queue[0][1:])

    # Use the Huffman codes to compress the text
    compressed_text = "".join([huffman_codes[char] for char in text])

    return compressed_text, huffman_codes

def decompress_text(compressed_text, huffman_codes):
    # Create a reverse mapping of the Huffman codes
    reverse_huffman_codes = {code: char for char, code in huffman_codes.items()}

    # Use the reverse mapping to decompress the text
    current_code = ""
    decompressed_text = ""
    for char in compressed_text:
        current_code += char
        if current_code in reverse_huffman_codes:
            decompressed_text += reverse_huffman_codes[current_code]
            current_code = ""

    return decompressed_text

# Test the compressor
text = "This is a test."
compressed_text, huffman_codes = compress_text(text)
decompressed_text = decompress_text(compressed_text, huffman_codes)
print("Original text:", text)
print("Compressed text:", compressed_text)
print("Decompressed text:", decompressed_text)
