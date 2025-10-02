

filename = 'simple.txt'

# Initialize counters
num_chars = 0
num_words = 0
num_lines = 0

# Open and process the file
with open(filename, 'r') as file:
    for line in file:
        num_lines += 1
        num_chars += len(line)
        num_words += len(line.split())

# Print the results
print(f"Number of characters: {num_chars}")
print(f"Number of words: {num_words}")
print(f"Number of lines: {num_lines}")

