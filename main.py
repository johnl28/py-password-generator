import random

def GeneratePassword(length, symbols, numbers, capitals):
  password = ""
  while len(password) < (length):
    if symbols:
      password += chr(random.randint(33, 47))
      symbols -= 1
    elif numbers:
      password += str(random.randint(0, 10))
      numbers -= 1
    elif capitals:
      password += chr(random.randint(65, 90))
      capitals -= 1
    else:
      if (capitals or numbers or symbols):
        continue
      password += chr(random.randint(65, 90)).lower()

  newPassword = ""
  while len(password):
    index = random.randint(0, len(password)-1)
    newPassword += password[index]
    password = password[:index] + password[index+1:] if len(password) != 1 else ""
  return newPassword


for x in range(10):
  print(GeneratePassword(20, 5, 1, 5))



