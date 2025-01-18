import random

user_win = 0
computer_win = 0

options = ["stone","paper","scissors"]


while True:
    user_input = input(" CHOOSE STONE/PAPER/SCISSORS or Q to quit: ").lower()
    if user_input == "q":
        break


    if user_input not in ["stone","paper","scissors"]:
        continue

    random_number = random.randint(0,2)
    # 0 is for stone , 1 is for stone , 2 is for the scissors 
    computer_pick = options[random_number]
    print("COMPUTER PICKED ", computer_pick + ",")


    if user_input == "stone" and computer_pick == "scissors":
        print("YOU WON THE MATCH")
        user_win += 1
        

    elif user_input == "paper" and computer_pick == "stone":
        print("YOU WON THE MATCH")
        user_win += 1
        

    elif user_input == "scissors" and computer_pick == "paper":
        print("YOU WON THE MATCH")
        user_win += 1
        

    else:
        print("YOU LOST THE MATCH")
        computer_win += 1

print ("YOU WON ",user_win, "and", "COMPUTER WON ",computer_win)
print("GOOD GAME. HAVE A GOOD DAY AHEAD")

