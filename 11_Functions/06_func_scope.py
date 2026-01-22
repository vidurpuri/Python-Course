#explain local and global scope in functions
# Local and Global Scope in Functions
# In Python, the scope of a variable refers to the region of the code where that variable is accessible. There are two main types of scope: local and global.
# 1. **Local Scope**:
#    - Variables defined inside a function are in the local scope of that function.
#    - They can only be accessed within that function.
#    - Once the function execution is complete, these variables are destroyed and cannot be accessed outside
#      the function.
# 2. **Global Scope**:
#    - Variables defined outside of any function are in the global scope.
#    - They can be accessed from anywhere in the code, including inside functions.
#    - If you want to modify a global variable inside a function, you need to use the `global` keyword.
# Example:
def local_scope_example():
    local_var = "I am local"
    print(local_var)  # This will work
local_scope_example()  # This will show local variables

def global_scope_example():
    global global_var
    global_var = "I am global"
    print(global_var)  # This will work
    # Uncommenting the next line will raise an error if global_var is not defined
   # print(another_global_var)  # This will raise an error if another_global_var is not defined
global_scope_example()  # This will show global variables