import random

AI = ["rock", "paper", "scissors"]

while True:
    

    random_choice = random.choice(AI)
    print(f"AI chose: {random_choice}")

    user = input("enter the choice rock, paper, scissors: ").lower()

    if user == random_choice:
        print("It's a tie!")
        
    elif(user == "rock" and random_choice == "scissors") or \
        (user == "paper" and random_choice == "rock") or \
        (user == "scissors" and random_choice == "paper"):
        print("You win!")
        
    elif(user == "stop"):
        break
        
    else:
        print("You lose!") 
    


