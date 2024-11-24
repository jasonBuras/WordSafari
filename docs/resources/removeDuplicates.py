# Define a function to remove words from allowed.txt if they appear in wordlist.txt
def filter_allowed_words(allowed_file_path, wordlist_file_path):
    # Read wordlist.txt
    with open(wordlist_file_path, 'r') as f:
        wordlist = set(f.read().splitlines())
    
    # Read allowed.txt
    with open(allowed_file_path, 'r') as f:
        allowed = set(f.read().splitlines())
    
    # Remove words from allowed that also appear in wordlist
    filtered_allowed = allowed - wordlist
    
    # Write the updated allowed list back to allowed.txt
    with open(allowed_file_path, 'w') as f:
        f.write("\n".join(sorted(filtered_allowed)))

# Paths to the text files
allowed_file_path = "allowed.txt"
wordlist_file_path = "wordlist.txt"

# Run the function to update allowed.txt
filter_allowed_words(allowed_file_path, wordlist_file_path)

print("Filtered allowed.txt to remove any words that appear in wordlist.txt.")
