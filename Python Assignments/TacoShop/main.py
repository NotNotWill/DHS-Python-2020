ulttaco = 6.79
tengal = 4.23
mstufburr = 9.57

name =input("Hello, Who might I be speaking to today: ")

print("Hello "+name)

uta = input("Enter the amount of Ultimate Tacos you would like today: ")
uta= int(uta)  

tghd = input("Enter the amount of 10 Gallon Hat Drinks you would like? ")
tghd = int(tghd) 

msb = input("Enter the amount of Mega Stuffed Burritos you would like? ")
msb = int(msb)

totaltaco = uta * ulttaco
totaltengal = tengal * tghd
totalmegstufburr = mstufburr * msb

completetotal = totalmegstufburr + totaltaco +  totaltengal

# Result with text
print("Your total for everything will be $" + str(completetotal))