#animals = ["dog","cat","liger","dragon"]
#
#animals.sort()
#print(animals[0])
#
#animals.append("squirrel")
#
#for pet in animals:
#  print(pet)
#  if pet =="liger":
#    print("This is not a pet")
#  else:
#    print("This is a pet")

hw = []
qz = []

homework1 = input("Enter a homework grade: ")
homework2 = input("Enter a homework grade: ")
homework3 = input("Enter a homework grade: ")
quiz1 = input("Enter a quiz grade: ")
quiz2 = input("Enter a quiz grade: ")
quiz3 = input("Enter a quiz grade: ")
quiz4 = input("Enter a quiz grade: ")
quiz5 = input("Enter a quiz grade: ")

homework1 = float(homework1)
homework2 = float(homework2)
homework3 = float(homework3)
quiz1 = float(quiz1)
quiz2 = float(quiz2)
quiz3 = float(quiz3)
quiz4 = float(quiz4)
quiz5 = float(quiz5)

hw.append(homework1)
hw.append(homework2)
hw.append(homework3)
qz.append(quiz1)
qz.append(quiz2)
qz.append(quiz3)
qz.append(quiz4)
qz.append(quiz5)

#print(max(hw))
#print(min(hw))
#print(sum(hw))
#print(len(hw))
averagehwb = sum(hw)/len(hw)
averageqzb = sum(qz)/len(qz)

averagehwa = averagehwb * 0.25
averageqza = averageqzb * 0.75

totalaverage = averagehwa+averageqza

print("Your total average is " + str(totalaverage))

#for value in range(2,10):
# print(value)