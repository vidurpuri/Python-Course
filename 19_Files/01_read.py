from pathlib import Path

file_path = Path(__file__).parent / 'vidur.txt'

try:
	with file_path.open('r') as f:
		print(file_path)
		content = f.read()
		print(content)
except FileNotFoundError:
	print(f"File '{file_path.name}' not found; creating an empty file at {file_path}.")
	file_path.touch()