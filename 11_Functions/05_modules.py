#Types of Modules
# 1. Built-in Modules: These are modules that come with Python, such as `math`, `os`, and `sys`. They provide a wide range of functionalities that can be used directly in your code.
# 2. Third-party Modules: These are modules created by the Python community and can be installed via package managers like `pip`. Examples include `requests`, `numpy`, and `pandas`.
# 3. Custom Modules: These are modules that you create yourself. You can define functions, classes, and variables in a Python file and import them into other Python files as needed.
# 4. Standard Library Modules: These are part of the Python Standard Library and provide a  wide range of functionalities. They include modules like `datetime`, `json`, and `re` (regular expressions).

import math
import external_module  # Importing a custom module
import requests

print("Square root of 16 is:", math.sqrt(16))  # Using the built-in math module
external_module.Hello()  # Calling a function from the external module
r = requests.get('https://api.github.com')  # Using the requests module to make an HTTP GET request
print("Response from GitHub API:", r.json())  # Print the JSON response from the API
