from random_word import RandomWords
from replit import clear

# Generate a random word
random_words = RandomWords()
word = list(random_words.get_random_word())

# Game variables
display = list()
letters = list()
status = True
lives = 7

# Guess display
for _ in word:
  display.append("_")

while status:

  print("Guessed letters: " + ' '.join(letters))
  guess = input("Guess a letter? ")

  if len(guess) > 1:
    print("Invalid, please guess one letter")

  if guess in display:
    clear()
    for x in letters:
      if guess == x:
        print("You have already guessed this letter")
    print(' '.join(display))

  elif guess in word:
    clear()
    positions = [i for i, x in enumerate(word) if x == guess]
    for x in positions:
      display[x] = guess
    letters.append(guess)
    letters.sort()
    print(f"The word does contain the letter {guess}")
    print(' '.join(display))

    if display == word:
      clear()
      print("Congratulations, you won!")
      print(' '.join(display))
      status = False

  else:
    clear()
    print(f"The word does not contain the letter {guess}")
    letters.append(guess)
    letters.sort()
    lives = lives - 1
    print(f"Total lives: {lives}")

    if lives == 0:
      clear()
      print("You lost, game over!")
      status = False