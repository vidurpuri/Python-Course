from pathlib import Path

file_path = Path(__file__).parent / 'python.txt'
with file_path.open('w') as f:
    f.write("Hello, this is a sample text file.\n")