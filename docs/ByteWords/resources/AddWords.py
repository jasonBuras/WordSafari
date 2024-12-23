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

    # Update the listbox views
    update_listboxes()

    # Clear the entry field
    word_entry.delete(0, tk.END)

# Function to update the listboxes
def update_listboxes():
    # Clear the listboxes first
    wordlist_listbox.delete(0, tk.END)
    allowed_listbox.delete(0, tk.END)

    # Insert words from the wordlist into the wordlist_listbox
    for word in load_wordlist(wordlist_file_path):
        wordlist_listbox.insert(tk.END, word)

    # Insert words from the allowed list into the allowed_listbox
    for word in load_wordlist(allowed_file_path):
        allowed_listbox.insert(tk.END, word)

# Function to move selected words from allowed to wordlist
def move_to_wordlist():
    selected_indices = allowed_listbox.curselection()

    # If no selection is made, simply return
    if not selected_indices:
        return

    # Load the word lists
    allowed = load_wordlist(allowed_file_path)
    wordlist = load_wordlist(wordlist_file_path)

    # List of words selected to move
    selected_words = [allowed[i] for i in selected_indices]

    # Remove selected words from 'allowed' and add them to 'wordlist'
    for word in selected_words:
        allowed.remove(word)
        wordlist.append(word)

    # Save the updated word lists
    save_wordlist(wordlist_file_path, wordlist)
    save_wordlist(allowed_file_path, allowed)

    # Update the listbox views
    update_listboxes()

# Function to move selected words from wordlist to allowed
def move_to_allowed():
    selected_indices = wordlist_listbox.curselection()

    # If no selection is made, simply return
    if not selected_indices:
        return

    # Load the word lists
    allowed = load_wordlist(allowed_file_path)
    wordlist = load_wordlist(wordlist_file_path)

    # List of words selected to move
    selected_words = [wordlist[i] for i in selected_indices]

    # Remove selected words from 'wordlist' and add them to 'allowed'
    for word in selected_words:
        wordlist.remove(word)
        allowed.append(word)

    # Save the updated word lists
    save_wordlist(wordlist_file_path, wordlist)
    save_wordlist(allowed_file_path, allowed)

    # Update the listbox views
    update_listboxes()

# Create the GUI
root = tk.Tk()
root.title("Word List Manager")

# Set the size of the window
root.geometry("600x400")

# Label and Entry to add a word
word_label = tk.Label(root, text="Enter a word to add to wordlist (Must be 5 characters):")
word_label.pack(pady=10)
word_entry = tk.Entry(root, width=30)
word_entry.pack(pady=5)

# Button to add the word
add_button = tk.Button(root, text="Add Word", command=add_word)
add_button.pack(pady=10)

# Frame to hold listboxes and buttons
list_frame = tk.Frame(root)
list_frame.pack(pady=10)

# Label for wordlist.txt
wordlist_label = tk.Label(list_frame, text="Wordlist (Possible Answers):")
wordlist_label.grid(row=0, column=0, padx=10)

# Frame for wordlist listbox and scrollbar
wordlist_frame = tk.Frame(list_frame)
wordlist_frame.grid(row=1, column=0, padx=10)

# Listbox for wordlist.txt
wordlist_listbox = tk.Listbox(wordlist_frame, selectmode=tk.MULTIPLE, width=30, height=10)
wordlist_listbox.pack(side=tk.LEFT)

# Scrollbar for wordlist.txt
wordlist_scrollbar = tk.Scrollbar(wordlist_frame, orient=tk.VERTICAL, command=wordlist_listbox.yview)
wordlist_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Link the scrollbar to the listbox
wordlist_listbox.config(yscrollcommand=wordlist_scrollbar.set)

# Buttons to move words between lists
button_frame = tk.Frame(list_frame)
button_frame.grid(row=1, column=1, padx=10)

move_right_button = tk.Button(button_frame, text=">>", command=move_to_allowed)
move_right_button.pack(pady=5)

move_left_button = tk.Button(button_frame, text="<<", command=move_to_wordlist)
move_left_button.pack(pady=5)

# Label for allowed.txt
allowed_label = tk.Label(list_frame, text="Allowed Words (Not Answers):")
allowed_label.grid(row=0, column=2, padx=10)

# Frame for allowed listbox and scrollbar
allowed_frame = tk.Frame(list_frame)
allowed_frame.grid(row=1, column=2, padx=10)

# Listbox for allowed.txt
allowed_listbox = tk.Listbox(allowed_frame, selectmode=tk.MULTIPLE, width=30, height=10)
allowed_listbox.pack(side=tk.LEFT)

# Scrollbar for allowed.txt
allowed_scrollbar = tk.Scrollbar(allowed_frame, orient=tk.VERTICAL, command=allowed_listbox.yview)
allowed_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Link the scrollbar to the listbox
allowed_listbox.config(yscrollcommand=allowed_scrollbar.set)

# Load the initial lists into the listboxes
update_listboxes()

# Start the main loop
root.mainloop()