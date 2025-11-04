# A Python script that calculates the simple interest earned on an investment over a period of time

principal = eval(input("Enter the principal amount: "))
rate = eval(input ("Enter the annual interest rate (in %): "))
time = eval(input("Enter the time the money is invested for (in years): "))

interest = principal * rate * time 

print(f"The simple interest is: {interest}")