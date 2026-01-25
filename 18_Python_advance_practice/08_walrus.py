# Use the walrus operator to read input until 'quit' is entered
while(testt := input("enter something")) != 'quit':
    print(testt)


# Use the walrus operator to find lengths of words which are greater than 4

words = ["python", "java", "c++", "ai"]

lengths = [n for w in words if (n:= len(w)) > 4]
print(lengths)
