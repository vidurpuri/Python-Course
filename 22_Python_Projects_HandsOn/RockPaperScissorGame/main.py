
'''
Workflow: 
1. User Select  Rock, Paper, Scissor
2. Computer Select random;y from Rock, Paper, Scissor
3. Print result

CASES : 
 1. Rock
    a. Rock - Rock = Tie
    b. Rock - Paper = Paper Win
    c. Rock - Scissor = Scissor Win

2. Paper
    a. Paper - Rock = Paper Win
    b. Paper - Paper = Tie
    c. Paper - Scissor = Scissor Win

3. Scissor
    a. Scissor - Rock = Rock Win
    b. Scissor - Paper = Paper Win
    c. Scissor - Scissor = Tie


'''
import random

options = ['Rock','Paper','Scissor']

user_Selection = input('Enter your choice: Rock , Paper or Scissor: ')
print(user_Selection)
computer_Selection = random.choice(options)
print(computer_Selection)

# Case 1 - User Selects ROCK
if(user_Selection == 'Rock' and computer_Selection == 'Rock'):
    print('Nobody Wins !! Its a Tie')
elif(user_Selection == 'Rock' and computer_Selection == 'Paper'):
    print('Computer Wins !!')
elif(user_Selection == 'Rock' and computer_Selection == 'Scissor'):
    print('User Wins !!')

# Case 2 - User Selects Paper
if(user_Selection == 'Paper' and computer_Selection == 'Paper'):
    print('Nobody Wins !! Its a Tie')
elif(user_Selection == 'Paper' and computer_Selection == 'Scissor'):
    print('Computer Wins !!')
elif(user_Selection == 'Paper' and computer_Selection == 'Rock'):
    print('User Wins !!')

# Case 3 - User Selects Scissor
if(user_Selection == 'Scissor' and computer_Selection == 'Scissor'):
    print('Nobody Wins !! Its a Tie')
elif(user_Selection == 'Scissor' and computer_Selection == 'Rock'):
    print('Computer Wins !!')
elif(user_Selection == 'Scissor' and computer_Selection == 'Paper'):
    print('User Wins !!')




