import string

def encrypt(amount, message):
  alphabet = list(string.ascii_lowercase)
  position = [(alphabet.index(letter) + int(amount)) for letter in message]
  word = [print(alphabet[x], end="") for x in position]
  return word

def decrypt(amount, message):
  alphabet = list(string.ascii_lowercase)
  position = [(alphabet.index(letter) - int(amount)) for letter in message]
  word = [print(alphabet[x], end="") for x in position]
  return word

while True:
  try:
    message = input("Type your message? ")
    amount = input("Shift number? (Max 7) ")
    direction = input("'encode' to encrypt or 'decode' to decrypt? ").lower()
    
    if direction == "encode":
      encrypt(amount, message)
      print("\n")
    elif direction == "decode":
      decrypt(amount, message)
      print("\n")
  
  except:
    print("Invalid input")