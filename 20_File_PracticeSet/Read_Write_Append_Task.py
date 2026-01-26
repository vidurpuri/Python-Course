from pathlib import Path

file_path = Path(__file__).parent / 'tasks.txt'

with file_path.open('w') as f:
    f.write('Task file is created')
    f.write('\nThis is the first task.')
    f.write('\nThis is the second task.')

with file_path.open('a') as f:
    f.write('\nThis is the third task.')

with file_path.open('r') as f:
    content = f.readlines()
    print(content)