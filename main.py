from game_data import data
import random

def get_data(data_list):
    return random.choice(data_list)

def compare_input(choice, a, b):
    if(a["follower_count"] > b["follower_count"]):
        higher = "A"
    else:
        higher = "B"
    if(higher == choice):
        return False
    else:
        return True

Flag = True

while Flag:
    a = get_data(data)
    b = get_data(data)
    is_wrong = False
    score = 0
    while not is_wrong:
        a = b
        b = get_data(data)
        if(a == b):
            b = get_data(data)
        print(f"compare A: {a['name']}, {a['description']}, {a['country']}")
        print("\n VS \n")
        print(f"compare B: {b['name']}, {b['description']}, {b['country']}")
        user_input = input("who has more followers? Type 'A' or 'B'")
        while not (user_input == "A" or user_input == "B"):
            print('Please enter either "A" or "B"')
            user_input = input("who has more followers? Type 'A' or 'B'")
        is_wrong = compare_input(user_input, a, b)
        
        if(not is_wrong):
            score += 1
            print(f"right answer your score is: {score}")
        else:
            print("wrong answer game over")
    paly_again = input("do you want to play again type yes or no").lower()
    if(paly_again == "no"):
        Flag = False
