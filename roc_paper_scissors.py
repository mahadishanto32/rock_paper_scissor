import random
user_choice = int(input("Enter your choice : Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

if user_choice >=3 or user_choice < 0:
    print("You Enter an Invalid Number, Please choice a Number Between 0-2")
else:
    computer_choice = random.randint(0,2)
    print("Computer Choice:")
    print(computer_choice)

    if computer_choice == user_choice:
        print("It's a Draw.")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose.")
    elif computer_choice == 2 and user_choice == 0:
        print("You Win.")
    elif computer_choice > user_choice:    
        print("You Lose.")
    elif user_choice > computer_choice:     
        print("You Win.")
        