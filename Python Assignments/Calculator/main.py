number1 =input("Enter a number: ")

number2 =input("Enter a number: ")

number1 = float(number1)
number2 = float(number2)

operation =input("What operation do you want to use? (1 = Addition, 2 = Subtraction, 3 = Multiplication, 4 = Division):   ")

operation = int(operation)

if operation == 1:
  result = number1+number2
  print(result)
if operation == 2:
  result = number1-number2
  print(result)
if operation == 3:
  result = number1*number2
  print(result)
if operation == 4:
  result = number1/number2
  print(result)

if operation > 4 or < 1:
  print("Error with input, please try again")
