# (5pts) Create a while loop that only prints out even numbers up to 20
start=0
while start < 21:
  print(start)
  start += 2

print(" ")
# (7.5pts) Create a while loop that counts up to 100 by 10s

start=0
while start < 101:
  print(start)
  start += 10

print(" ")
#(10pts) Create a while loop that runs 5 times and asks the users to enter a number every iteration. After the loop has run 5 times the total is printed to the console


starting_value = 0
if starting_value < 100:
    print("Starting value is",starting_value)
    str_value1 = input ("Enter a number: ")
    str_value2 = input ("Enter a number: ")
    str_value3 = input ("Enter a number: ")
    str_value4 = input ("Enter a number: ")
    str_value5 = input ("Enter a number: ")

    str_value1 = float(str_value1)
    str_value2 = float(str_value2)
    str_value3 = float(str_value3)
    str_value4 = float(str_value4)
    str_value5 = float(str_value5)

    alltotal = str_value1 + str_value2 + str_value3 + str_value4 + str_value5
    print("Total of all of these numbers is:",alltotal)

# (10pts) Create a while loop that runs 7 times and appends to a list. After the while loop is finished, the list is printed to the console.

items = []

item1 = input("Enter an item you need on your shopping list: ")
item2 = input("Enter an item you need on your shopping list: ")
item3 = input("Enter an item you need on your shopping list: ")
item4 = input("Enter an item you need on your shopping list: ")
item5 = input("Enter an item you need on your shopping list: ")
item6 = input("Enter an item you need on your shopping list: ")
item7 = input("Enter an item you need on your shopping list: ")

items.append(item1)
items.append(item2)
items.append(item3)
items.append(item4)
items.append(item5)
items.append(item6)
items.append(item7)

print("Your Shopping List Is:")

for item in items:
  print(item)
