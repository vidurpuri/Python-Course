'''
1. Start the program.

2. Define the history filename (for example, "history.txt").

3. Enter an infinite loop (while True) to repeatedly accept user input.

4. Prompt the user to enter either a calculation (e.g., "8 + 5") or one of the 
   commands: "history", "clear", "exit".

5. If the user enters "exit":

   a. Print a goodbye message.
   b. Break the loop and end the program.

6.If the user enters "history":

   a. Try to open the history file for reading.
   b. If the file exists and is not empty, print each saved line (each previous calculation).
   c. If the file does not exist or is empty, print "No history found".
   d. Continue to the next iteration of the loop.

7. If the user enters "clear":

   a. Open the history file for writing (this overwrites it) to empty its contents.
   b. Print "History cleared".
   c. Continue to the next iteration of the loop.

8.Otherwise (assume the user entered a calculation):

   a. Try to parse the input into two numbers and an operator (you can split by spaces, e.g., "8 + 5").
   b. If parsing fails or the input is invalid, print "Invalid input" and continue to the next loop iteration.
   c. Perform the calculation by checking the operator:
       -- If "+", add.
       -- If "-", subtract.
       --If "*", multiply.
       -- If "/", divide (check for division by zero and handle with an error message).
   d. Print the result.
   e. Append the calculation and result (formatted as desired) to the history file.
   f. Continue the loop for the next input.
9. End when the user chooses "exit".
'''
from pathlib import Path

history_file = 'history.txt'

file_path = Path(__file__).parent / history_file

def user_exit():
    print('GOODBYE !!')

def user_history():
    if(file_path.exists):
        with file_path.open('r')as f:
            content = f.read()
            print(content)
    else:
        print('No History file found')

def user_clear():
    if(file_path.exists):
        with file_path.open('w')as f:
            f.write('')
            print('History Cleared')

def user_Calc(expression):
    break_exp = expression.split(' ')
    if len(break_exp) != 3:
        print('Invalid input')
        return
    num1 = int(break_exp[0])
    operator = break_exp[1]
    num2 = int(break_exp[2])
    result = 0
    
    
    match operator:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            result = num1 / num2
    
    exp_with_result = f'{expression} = {result}'
    print(exp_with_result)
    with file_path.open('a') as f:
        f.write(f'\n{exp_with_result}')

while True:
    user_input = input('Please enter either a calculation (e.g., "8 + 5") or one of the commands: "history", "clear", "exit": ')
    match user_input:
        case 'history':
            print('History')
            user_history()
        case 'exit':
            print('exit')
            user_exit()
            break
        case 'clear':
            print('clear')
            user_clear()
            
        case _:
            print(f'expression: {user_input}')
            user_Calc(user_input)
    


