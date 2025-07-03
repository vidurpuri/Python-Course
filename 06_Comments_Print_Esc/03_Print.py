# Any word after , will be printed as it is with by default space in between.
print('Hello World',"Vidur",5) # prints Hello World Vidur 5

# here the sep parameter is set to '-', so the output will use a hyphen to separate each argument.
#  As a result, the output will be:prints Hello World-Vidur-5
print('Hello World', 'Vidur', 5, sep='-') 


#Every print statement in Python ends with a newline character by default.
print('Hello World') # prints Hello World
print('Vidur') # prints Vidur

# If you want to change this behavior, you can use the end parameter.   
print('Hello World', end=' ') # prints Hello World
print('Vidur', end=' ') # prints Vidur