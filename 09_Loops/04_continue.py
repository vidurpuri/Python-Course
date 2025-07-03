for i in range(1, 11):
    if i == 6:
        print("Skipping the iteration at i =", i)
        continue  # Skip the rest of the loop when i is 6
    print("Iteration:", i)