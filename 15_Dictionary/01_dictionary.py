marks = {"Vidur":78, "Jack": 45, "Rahul": 89}

print(marks["Vidur"]) # Access dictionalry value through its key

#Get all keys 
print(marks.keys())

#Get all values 
print(marks.values())

marks.clear() # Empties a dictionary

# Dictionary Comprehension

# Print table of 5 in key value pair

table_of_5 = {i:5*i for i in range(1,11)}
print(table_of_5)
#Output = {1: 5, 2: 10, 3: 15, 4: 20, 5: 25, 6: 30, 7: 35, 8: 40, 9: 45, 10: 50}