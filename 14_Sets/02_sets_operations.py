# Define Union and intersection

a = {3,4,5,6,7}
b = {3,6,8,9}

#Union
c = a.union(b) # Provide all elements from a and b with no duplicates 
print(c)

#Intersection
d = a.intersection(b) # Provide all elements from a and b which are common 
print(d)

#Difference
e = a.difference(b) # Provides all elements of a whoch are not present in b 
print(e) 