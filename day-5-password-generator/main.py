import string, random


def random_string(length):
  letters = string.ascii_letters
  result = ''.join(random.choice(letters) for i in range(length))
  return result


def random_number(length):
  numbers = string.digits
  result = ''.join(random.choice(numbers) for i in range(length))
  return result


def random_symbol(length):
  symbols = string.punctuation
  result = ''.join(random.choice(symbols) for i in range(length))
  return result


def password_shuffle(string):
  password = list(string)
  random.shuffle(password)
  result = ''.join(password)
  return result


while True:
  print("Password generator")

  password = random_string(int(input("How many letters? ")))
  password += random_number(int(input("How many numbers? ")))
  password += random_symbol(int(input("How many symbols? ")))

  print(password_shuffle(password))