test = input("Please enter your test average: ")
quiz = input("Please enter your quiz average: ")
homework = input("Please enter your homework average: ")

test = int(test)
quiz = int(quiz)
homework = int(homework)

testresult = (test*0.5)
quizresult = (quiz*0.3)
homeworkresult = (homework*0.2)

total = testresult+quizresult+homeworkresult

if total > 89:
  print("You got an A")


elif total > 82:
  print("You got a B")


elif total > 72:
  print("You got a C")

elif total > 67:
  print("You got a D")

else:
  print("You failed :(")


###############################################

