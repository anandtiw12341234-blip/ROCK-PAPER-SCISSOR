import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter Your Move = Rock , Paper , Scissor =")
comp_choice = random.choice(item_list)

print(f"User Choice ={user_choice}, Computer Choice = {comp_choice}")

if   user_choice == comp_choice:
    print("Both Chooses Same: = Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Papaer Covers Rock = Computer Win")
    else:
        print("Rock Broke Scissor = You Win")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor Cuts Papaer , Computer Win")
    else:
        print("Papers Covers Rock, You Win")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor Cuts Paper, You Win")
    else:
        print("Rock Broke Scissor , Computer Win")