import random
print("number guessing game")
number=random.randint(1, 9)
chances=0
print (" guess a number between (1 and 9)")
while chances <5:
  guess = int(input("enter your guess:-"))
  if guess == number:
    print (" Congrats You Won!!")
    break
  elif guess< number:
    print (" your guess was too low, guess a number higher than", guess)
  else:
    print (" your guess was too high, guess a number lower than", guess)
chances += 1
if chances >5:
  print(" You Lose,the number is", number)
