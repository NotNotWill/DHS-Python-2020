listOfTest = []
test1 = input("Please enter a test grade: ")
test2 = input("Please enter a test grade: ")
test3 = input("Please enter a test grade: ")
test4 = input("Please enter a test grade: ")
test5 = input("Please enter a test grade: ")

test1 = float(test1)
test2 = float(test2)
test3 = float(test3)
test4 = float(test4)
test5 = float(test5)

listOfTest.append(test1)
listOfTest.append(test2)
listOfTest.append(test3)
listOfTest.append(test4)
listOfTest.append(test5)

for grade in listOfTest:
  if grade % 2 == 1:
    print("Grade is odd.")
  if grade % 2 == 0:
    print("Grade is even.")

print("Highest grade was a ",max(listOfTest))
print("Lowest grade was a",min(listOfTest))
print("The sum of all the tests is",sum(listOfTest))

average = sum(listOfTest)/5

print("The average of all of the tests is",(average))