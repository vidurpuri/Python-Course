# list 
# A list is a collection of items that can be of different types.
# Lists are mutable, meaning you can change their content.
# Lists are ordered, meaning the items have a defined order, and that order will not change unless you explicitly reorder the list.
# Lists are iterable, meaning you can loop through them.
# Lists can contain duplicate items.


marks = [5,2,11,4,6]
extra_marks = [3,6,8]

marks.append(10)  # Add an item to the end of the list
marks.pop(3) # Removes last item from list + any mentioned index as well
marks.insert(1,9) # insert new data at [index] 
marks.remove(2) # removes list item  mentioned 
marks.extend(extra_marks) # append another list to existing list

print(marks)