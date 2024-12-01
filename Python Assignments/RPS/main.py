import random
comchoice = random.randint(1, 3)

userscore = 0
comscore = 0

while True:
  userchoice = input("Choose: 1 - rock; 2 - Paper; 3 - Scissors: ")

  userchoice = int(userchoice)
  comchoice = int(comchoice)
# Rock
  if comchoice == 1:
    if userchoice == 2:
      print("Paper Covers Rock, You Win")
      userscore = userscore+1
    elif userchoice == 3:
     print("Rock smashes scissors, you lose!")
     comscore=comscore+1
    else:
      print("Tie")
# Paper
  elif comchoice == 2:
    if userchoice == 1:
      print("Paper Covers Rock, You Lose")
      comscore=comscore+1
    elif userchoice == 3:
      print("Scissors cut paper, You Win!")
      userscore = userscore+1 
    else:
      print("Tie")
# Scissors
  elif comchoice == 3:
    if userchoice == 1:
      print("Rock Smashes scissors, you win")
      userscore = userscore+1
    elif userchoice == 2:
      print("Scissors cut paper, You lose")
      comscore=comscore+1
    else:
      print("Tie")
  print("Computer score:",comscore)
  print("Your Score",userscore)