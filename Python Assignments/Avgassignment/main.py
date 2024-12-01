test1 = input("Please enter a test grade: ")
test2 = input("Please enter another test grade: ")

test1 = int(test1)
test2 = int(test2)

total = test1+test2*0.5

if total > 89:
  print("You got an A")

elif total > 82:
  print("You got a B")

elif total > 72:
  print("You got a C")

elif total < 67:
  print("You got a D")

else:
  print("You failed :(")