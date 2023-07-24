# futval.py
# A program to compute the value of an investment
# carried 10 years inot the future
# By Jaden Atwater, June 13, 2023

def main():
    print("This program calculates the future value of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual intereest rate: "))
    year = eval(input("Enter the amount of years:"))

    for i in range(10):
        principal = principal * (1 + apr)

    print ("The value in 10 years is:", principal)

main()