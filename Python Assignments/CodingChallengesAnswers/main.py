print("*")
print("* *")
print("* * *")
print("* * * *")
print("* * * * *")
print("* * * *")
print("* * *")
print("* *")
print("*")

### Using If and Else Statements
username = input("Enter Your Name: ")

if username == "Bond":
  print("Welcome on board 007")
elif username == "bond":
  print("Welcome on board 007")
else:
  print("Good Morning",username)

# Months
month = input("Enter Month: ")
if month == "January":
  print("31 Days")
elif month == "February":
  print("28/29 Days")
elif month == "March":
  print("31 Days")
else:
  print("Invalid")

# Dog years problem
age = input("enter age of dog: ")
age = int(age)

if age < 3:
  dogYears = age * 10.5
  print(dogYears)
elif age > 2:
  dogYears = age*4+10.5
  print(dogYears)
else:
  print("Invalid.")