# Description: This script demonstrates basic file operations in Python. 
# Task: Create a text file, write a line of text to it, and then read the text back.

from pathlib import Path

file_path = Path(__file__).parent / 'notes.txt'

with file_path.open('w') as f:
    f.write("Learning Python is fun !")

with file_path.open('r') as f:
    content = f.read()
    print(content)