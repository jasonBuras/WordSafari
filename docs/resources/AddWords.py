import tkinter as tk
from tkinter import messagebox
import os

# File paths for word lists
allowed_file_path = "allowed.txt"
wordlist_file_path = "wordlist.txt"

# Function to load words from files and keep them sorted
def load_wordlist(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            words = f.read().splitlines()
            return sorted(set(words))
    return []

# Function to save the updated word lists
def save_wordlist(file_path, words):
    with open(file_path, 'w') as f:
        f.write("\n".join(sorted(set(words))))

# Function to add a word to wordlist.txt
def add_word():
    new_word = word_entry.get().strip().lower()

    # Check if the input is empty
    if not new_word:
        messagebox.showerror("Input Error", "Please enter a word.")
        return

    # Check if the word length is exactly 5 letters
    if len(new_word) != 5:
        messagebox.showerror("Input Error", "The word must be exactly 5 letters long.")
        return

    # Load the current word lists
    wordlist = load_wordlist(wordlist_file_path)
    allowed = load_wordlist(allowed_file_path)

    # Check if word already exists in wordlist.txt
    if new_word in wordlist:
        messagebox.showinfo("Word Exists", f"'{new_word}' already exists in wordlist.txt.")
        return

    # If the word exists in allowed.txt, move it to wordlist.txt
    if new_word in allowed:
        allowed.remove(new_word)
        wordlist.append(new_word)
        messagebox.showinfo("Word Added", f"'{new_word}' moved from allowed.txt to wordlist.txt.")
    else:
        # If the word doesn't exist in either file, add it to wordlist.txt
        wordlist.append(new_word)
        messagebox.showinfo("Word Added", f"'{new_word}' added to wordlist.txt.")

    # Save the updated lists and sort them
    save_wordlist(wordlist_file_path, wordlist)
    save_wordlist(allowed_file_path, allowed)

    # Clear the entry field
    word_entry.delete(0, tk.END)

# Create the GUI
root = tk.Tk()
root.title("Word List Manager")

# Set the size of the window
root.geometry("400x200")

# Label and Entry to add a word
word_label = tk.Label(root, text="Enter a word to add to wordlist (Must be 5 characters):")
word_label.pack(pady=10)
word_entry = tk.Entry(root, width=30)
word_entry.pack(pady=5)

# Button to add the word
add_button = tk.Button(root, text="Add Word", command=add_word)
add_button.pack(pady=10)

# Start the main loop
root.mainloop()
