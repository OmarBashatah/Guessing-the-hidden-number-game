import random 
n=int(input("enter your number between 1 and : "))
number=random.randint(1,n)
guess=int(input(f"enter your number between 1 and {n} "))

while guess != number:
  if guess>number:
    print("you guessed higher ")
    guess=int(input(f"enter your number between 1 and {n} "))


  elif guess<number:
    print("you guessed lower ")
    guess=int(input(f"enter your number between 1 and {n} "))

print("you guessed right ")