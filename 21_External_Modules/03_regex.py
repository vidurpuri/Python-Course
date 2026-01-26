import re

text = "The rain in Spain stays mainly in the plain."

#Search for pattern 
match = re.search('plain', text)
print(match)
if match:
    print("Match found!")
    print('Start Index:', match.start())
    print('End Index:', match.end())

# Find all occurence of a pattern
matches = re.findall('ain', text)
print("All Matches Found:", matches)

# replace text 

new_text = re.sub('plain', 'mountain', text)
print("Replaced Text:", new_text)