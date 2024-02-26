import random

def play_game():
  """
  This function plays a single round of Rock-Paper-Scissors.
  """
  # User input
  while True:
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice in ["rock", "paper", "scissors"]:
      break
    else:
      print("Invalid choice. Please try again.")

  # Computer selection
  computer_choice = random.choice(["rock", "paper", "scissors"])

  # Display choices
  print(f"You chose: {user_choice.capitalize()}")
  print(f"Computer chose: {computer_choice.capitalize()}")

  # Determine winner
  if user_choice == computer_choice:
    print("It's a tie!")
  elif (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "paper" and computer_choice == "rock") or \
       (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
  else:
    print("You lose!")

# Score tracking (optional)
# You can uncomment these lines to track scores
# user_score = 0
# computer_score = 0

# Play again prompt
while True:
  play_again = input("Play again? (y/n): ").lower()
  if play_again in ["y", "n"]:
    break
  else:
    print("Invalid choice. Please enter 'y' or 'n'.")

if play_again == "y":
  # Reset scores (if score tracking is enabled)
  # user_score = 0
  # computer_score = 0
  play_game()
else:
  print("Thanks for playing!")

if __name__ == "__main__":
  play_game()
