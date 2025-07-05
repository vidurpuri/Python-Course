# Define Sets in python
# Sets are unordered (the order of elements is not guaranteed).
# Sets do not allow duplicate elements.
# Sets are mutable, so you can add or remove elements after creation. 

my_set = {2,4,6,7,8,9}

my_set.add(3) # Add element in any place within set
my_set.remove(4) # Remove an element from a set; it must be a member. If the element is not a member, raise a KeyError.

#Remove an element from a set if it is a member.
# Unlike set.remove(), the discard() method does not raise an exception when an element 
# is missing from the set.
my_set.discard(10)

print(my_set)