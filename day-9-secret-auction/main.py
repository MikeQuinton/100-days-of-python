from replit import clear

proc = True
participants = {}

while proc:
  name = input("What is your name? ")
  bid = input("What is your bid? ")
  direction = input("Are there any other bids? (yes/no) ")
  participants[name] = bid
  clear()

  if direction == "yes":
    continue
  elif direction == "no":
    max_bid = max(participants.values())
    max_name = max(participants)
    print(f"The winner is {max_name} with a bid of £{max_bid}!")
    proc = False