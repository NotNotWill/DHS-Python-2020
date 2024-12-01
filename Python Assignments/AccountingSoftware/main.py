amountpay = input("Enter the amount you get paid: ")
hoursworked = input("Enter how many hours you worked this week: ")
print("You worked " + hoursworked + " at the rate of $" + amountpay + ".")

amountpay = float(amountpay)
hoursworked = float(hoursworked)

grosswage = amountpay * hoursworked
ftax = grosswage * 0.2
stax = grosswage * 0.053
paycheck = grosswage - ftax - stax

print("The Federal Tax is $" + str(ftax))
print("The State Tax is $" + str(stax))
print("Your total paycheck (after taxes) is $" + str(paycheck))