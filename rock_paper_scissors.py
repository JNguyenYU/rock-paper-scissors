import random

play = True
valid= True
user_score = 0
computer_score = 0



while play and valid:
    choice = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choice)
    user_choice = input("Enter either rock, paper, or scissors: ")
    if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors" :
        print("Not a valid option, please enter a valid answer")
        valid == False
    


    if user_choice == computer_choice:
        print("You chose " + user_choice + ", " + "computer chose " + computer_choice)
        print("It's a tie")
        print("Player: " + str(user_score) + " / " + "Computer: " + str(computer_score))

    elif user_choice.lower() == "rock":
        print("You chose " + user_choice + ", " + "computer chose " + computer_choice)
        if computer_choice.lower() == "scissors":
            print("Rock beats scissors, you win")
            user_score += 1
            print("Player: " + str(user_score) + " / " + "Computer: " + str(computer_score))
        else:
            print("Paper beats rock, you lose")
            computer_score += 1
            print("Player: " + str(user_score) + " / " + "Computer: " + str(computer_score))
        play_again = input("Would you like to play again? Enter y or n: ")
        if play_again == "n":
            play = False

    elif user_choice.lower() == "paper":
        print("You chose " + user_choice + ", " + "computer chose " + computer_choice)
        if computer_choice.lower() == "rock":
            print("Paper beats rock, you win")
            user_score += 1
            print("Player: " + str(user_score) + " / " + "Computer: " + str(computer_score))
        else:
            print("Scissors beat paper, you lose")
            computer_score += 1
            print("Player: " + str(user_score) + " / " + "Computer: " + str(computer_score))
        play_again = input("Would you like to play again? Enter y or n: ")
        if play_again == "n":
            play = False

    elif user_choice.lower() == "scissors":
        print("You chose " + user_choice + ", " + "computer chose " + computer_choice)
        if computer_choice.lower() == "paper":
            print("Scissors beat paper, you win")
            user_score += 1
            print("Player: " + str(user_score) + " / " + "Computer: " + str(computer_score))
        else:
            print("Rock beats scissors, you lose")
            computer_score += 1
            print("Player: " + str(user_score) + " / " + "Computer: " + str(computer_score))

        play_again = input("Would you like to play again? Enter y or n: ")
        if play_again == "n":
            play = False