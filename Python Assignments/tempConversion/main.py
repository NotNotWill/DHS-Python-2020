fahrenheit= input("Please enter the temperature in degrees Fahrenheit (Decimals are allowed): ")
celsius= input("Please enter the temperature in degrees Celsius (Decimals are allowed): ")
kelvin= input("Please enter the temperature in degrees Kelvin (Decimals are allowed): ")

fahrenheit= float(fahrenheit) 
celsius = float(celsius)
kelvin = float(kelvin)

ftok = (fahrenheit)-32*5/9+273.15
ctof = (celsius)*9/5+32
ktof = (kelvin)-273.15*9/5+32

print(str(fahrenheit)+" degrees Fahrenheit is "+str(ftok)+" degrees Kelvin.")
print(str(celsius)+" degrees Celsius is "+str(ctof)+" degrees Farenheight.")
print(str(kelvin)+" Kelvin is "+str(ktof)+" degrees Fahrenheit.")