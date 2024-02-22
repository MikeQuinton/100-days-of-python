import random

choices = {
  "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
  """,
  "paper": """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
  """,
  "scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
  """
}

while True:
  try:
    print("\nWelcome to rock, paper and scissors!")
    player = input("What do you choose? (rock, paper or scissors) ")
    computer = random.choice(list(choices.keys()))
  
    print(f"The player has chosen {player} \n {choices[player]}")
    print(f"The computer has chosen {computer} \n {choices[computer]}")
  
    if player == computer:
      print("It's a draw, try again!")
    elif player == "rock":
      if computer == "scissors":
        print("Congratulations, you won!")
      else:
        print("You lost, try again!")
    elif player == "paper":
      if computer == "rock":
        print("Congratulations, you won!")
      else:
        print("You lost, try again!")
    elif player == "scissors":
      if computer == "paper":
        print("Congratulations, you won!")
      else:
        print("You lost, try again!")
  except KeyError:
    print("Unknown value, please enter rock, paper or scissors to play!")