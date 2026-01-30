'''
WORKFLOW : 

1. Start the program.
2. Show a welcome message and the game rules.
3. Let the user choose a difficulty level.
    a. Based on the chosen level, set a list of possible secret words.
4. Randomly select a secret word from the chosen list.
5. Tell the user how many letters are in the secret word.
6. Initialize an attempt counter to 0.
7. While the user has not guessed the secret word:
    a. Ask the user to enter a guess.
    b. Increment the attempt counter.
    c. If the guess equals the secret word:
        i. Print “Congratulations!” and show the number of attempts.
        ii. Break the loop (end the game).
    d. Else (guess is incorrect):
        i. Compare each letter of the guess with the secret word.
        ii. Count how many letters are correct and in the correct position.
        iii. Provide feedback to the player (e.g., number of correct letters/in-place, optionally show matched letters and placeholders).
8. Optionally: allow replay or exit after the round ends.

'''
import random

easy = ['try', 'run', 'say', 'cat', 'dog', 'see']
medium = ['apple', 'sheep','count', 'break', 'select']
hard = ['feedback','appraisal','optional', 'matched', 'possible']
secret_word = ''

print('WELCOME TO THE TEXT PASSWORD GUESS GAME.\n')

difficulty = input('Choose the difficulty level: EASY, MEDIUM or HARD: ')

match difficulty:
    case 'EASY':
        secret_word = random.choice(easy)
    case 'MEDIUM':
        secret_word = random.choice(medium)
    case 'HARD':
        secret_word = random.choice(hard)

#print(f'Your chossen word as per selected difficulty is: {secret_word}')
print(f'HINT: Chosen word has {len(secret_word)} characters in it.')

counter = 0
while True:
    usr_guess = input('Please guess the word:')
    counter += 1
    hint = ''
    if(usr_guess == secret_word):
        print('You guessed right. CONGRATULATIONS !!')
        print(f'You took {counter} attempts.')
        break
    for i in range(len(secret_word)):
        print('will write logic')
        if(i < len(usr_guess) and usr_guess[i] == secret_word[i]):
            hint += usr_guess[i]
        else:
            hint += '_'

        print(f'HINT: {hint}')
print('GAME OVER')
