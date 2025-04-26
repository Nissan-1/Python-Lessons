import random
score = 0 
score2 = 0
for x in range(3):

 def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return user_choice

 def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

 def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        score += 1
        return "You win!"
    else:
        score2 += 1
        return "You lose!"

 def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

 if __name__ == "__main__":
    play_game()

print(f"Your score: {score}")
print(f"Computer score: {score2}")
if score > score2:
    print("You win the game!")
elif score == score2:
    print("It's a tie game!")
else:
    print("You lose the game!")
   