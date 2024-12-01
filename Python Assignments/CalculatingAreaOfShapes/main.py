shape = input("Please enter a shape (1-Square, 2-circle, 3-rectangle\n4-triangle): ")

shape = int(shape)

if shape == 1:
  side = input("Enter the base of the square: ")
  side = float(side)
  squarearea = side*side
  print("The area of the square is " + str(squarearea))

elif shape == 2:
  radius = input("Enter the radius: ")
  radius = float(radius)
  circlearea = radius*3.14159
  print("The area of the circle is " + str(circlearea))

elif shape == 3:
  reclength = input("Enter the length of the rectangle: ")
  recheight = input("Enter the height of the rectangle: ")
  reclength = float(reclength)
  recheight = float(recheight)
  recarea = recheight*reclength
  print("The area of the rectangle is " + str(recarea))

elif shape == 4:
  tribase = input("Enter the base of the triangle: ")
  triheight = input("Enter the height of the triangle: ")
  tribase = float(tribase)
  triheight = float(triheight)
  trianglearea = 0.5 * tribase * triheight
  print("The area of the square is " + str(trianglearea))

elif shape > 5:
  print("Error. Try again")