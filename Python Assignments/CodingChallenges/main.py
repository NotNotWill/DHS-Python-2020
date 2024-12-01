### Imports
import time
import random
### Using If and Else Statements
username = input("Enter Your Name: ")

if (username) == "Bond":
  print("Welcome on board 007")
elif (username) == "bond":
  print("Welcome on board 007")
else:
  print("Good Morning",(username))

time.sleep(3)
### Loops and Lists
target_num = random.randint(1, 11)

userint = input("Enter a random number 1-10: ")

if userint == target_num:
  print("You guessed correct!")

else:
  print("Incorrect. Try Again")

time.sleep(3)
### Printing Pattern

print("*")
print("**")
print("***")
print("****")
print("*****")
print("****")
print("***")
print("**")
print("*")

