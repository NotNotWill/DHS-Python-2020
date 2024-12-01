import random 
target_num = random.randint(1, 11)


userint = input("Enter a random number 1-10: ")

if userint == target_num:
  print("You guessed correct!")

else:
  print("Incorrect. Try Again")