'''
Step 1 — Import the random module: import random so you can pick random items from lists.

Step 2 — Create three lists with Indian examples: subjects (person names), actions (weird or attention-grabbing things), and places (real Indian cities or locations).

Step 3 — Randomly pick one item from each list: use random.choice(subjects), random.choice(actions), and random.choice(places).

Step 4 — Combine the chosen words into a headline: format them into a single string (e.g., f"{subject} {action} in {place}").

Step 5 — Print the headline to the user: display the generated headline.

Step 6 — Ask the user if they want another headline: prompt for yes/no input.

Step 7 — Repeat or stop: if the user says yes, loop back to Step 3; if no, exit the program.

'''
import random

subjects = ["Ravi", "Priya", "Arjun"]
actions = ["dancing with a coconut", "whispering to a mango tree", "wearing slippers on the head"]
places = ["Mumbai", "Jaipur", "Varanasi"]

def fakeNews():
    rand_sub = random.choice(subjects)
    rand_action = random.choice(actions)
    rand_places = random.choice(places)
    print(f'BREAKING NEW: {rand_sub} is {rand_action} in {rand_places}')



while True:
    fakeNews()
    yes_no = input('Do you wish to continue, YES/NO: ').strip()

    if(yes_no.lower() == 'no'):
        break
    

