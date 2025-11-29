# --------------- imports ----------------------- 
import random
from Questions import trivia

class User:
    def __init__(self, name, surname):
        self.name = name
        self.score = 0
        self.surname = surname

    def to_dict(self):
        return {
            'Name': self.name,
            'Surname': self.surname,
        }
    
    def add_score(self):
        self.score += 1

# --------------- User Inputs --------------------

name = input("Enter your name: ")
surname = input("Enter your surname: ")


# --------------- User Object Creation ------------
user = User(name, surname)

print(f"Welcome {user.name} {user.surname} to the Quiz Game!")

# --------------- Game Logic ----------------------
while True:
    try:
        rounds = int(input("Choose number of rounds (5, 10, or 15): "))
        if rounds in [5, 10, 15]:
            break
        else:
            print("Please choose a valid number of rounds.")
    except ValueError:
        print("Please enter a number.")
        
question_indexes = random.sample(range(1, 51), rounds)

print(f"Welcome {user.name} {user.surname} to the Quiz Game you have selected to play {rounds} rounds!")
current_round = 1

while current_round <= rounds:
    print(f"\nRound {current_round} of {rounds}")

    q_index = question_indexes[current_round - 1]
    question_data = trivia[q_index - 1]

    print(question_data["question"])
    
    for k in range(len(question_data["options"])):
        print(f"{chr(65 + k)}. {question_data['options'][k]}")

    answer = input("Your answer: ")
    if answer.strip().lower() == question_data["answer"].strip().lower():
        print("Correct!")
        user.add_score()
    else:
        print(f"Wrong! The correct answer was: {question_data['answer']}")
    current_round += 1
print(f"\nGame Over! Your total score is: {user.score} out of {rounds}")   

