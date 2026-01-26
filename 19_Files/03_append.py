from pathlib import Path

file_path = Path(__file__).parent / 'python.txt'
with file_path.open('a') as f:
    f.write("This text will be appended to the file.\n")