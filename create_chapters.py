import os

# Name of the text file containing the list of directory names
filename = "chapters.txt"

# Read in the list of directory names from the text file
with open(filename, "r") as f:
    directory_names = f.read().splitlines()

# Create each directory in the list
for i, name in enumerate(directory_names):
    os.makedirs(f"{i}-{name}", exist_ok=True)
    print(f"Created directory: {name}")
