# Keith Rochfort KR22090004774
# DS T07 Compulsort Task 1
# Capstone Project 1
# Two different financial calculators: an investment calculator and a home loan repayment calculator

# Start of code
import math

# Options list, in case other functions are added in later versions:
options = [
    'investment',
    'bond'
    ]

# Details of the options to be displayed
option_details = [
    'investment   -    to calculate the amount of interest you\'ll earn on your investment',
    'bond         -    to calculate the amount you\'ll have to pay on a home loan'
    ]

# Interest options in a list to iterate through
interest_options = [
    'simple',
    'compound'
]

# Empty user input string for a while loop to function and run if blank
user_input = ' ' 

# First line of the input text
input_text = "Type your choice of either 'investment' or 'bond' from the menu below to proceed:\n"

# for loop to list the investment or bond options
for detail in option_details:
    input_text += (f'\t{detail}\n')
# while loop to prompt for either 'investment' or 'bond' option and only accept the options given:
while user_input not in options:
    user_input = input(input_text).lower() # .lower() converts any user input to lowercase to match the listed options
print(f'You selected: {user_input}') # Gives a positive user response


# If 'investment' is chosen: 
# Variable user data to prompt to collect
if user_input == 'investment':
    deposit = float(input("Please enter the amount of money you will be depositing: "))
    interest_rate = float(input("Please enter the percentage interest rate as a number only, without the '%' sign: "))
    years = int(input("Please enter the number of years you plan on investing: "))
    # Ask if 'simple' or 'compound' interest applies:
    interest = ' '
    input_interest = 'Choose from the interest types shown below:\n'
    for option in interest_options:
        input_interest += f'\t{option}\n'
    while interest not in interest_options:
        interest = input(input_interest)
    print(f'You chose: {interest}')

    # Formulae, both round to 2dp for currency:
    # Simple interest: deposit * (1 + (interest_rate/100)*years)
    simple_interest_total = round(deposit*(1 + interest_rate/100 * years), 2)

    # Compound interest: deposit*((100+interest_rate)/100)**years)
    # Using the given formulae using math.pow:
    compound_interest_total = round(deposit*math.pow(((100+interest_rate)/100), years), 2)

    # if statements to print results:
    if interest == 'simple':
        print(f'Based on the information given, your return on investment will be:\n\tR{simple_interest_total}')
    elif interest == 'compound':
        print(f'Based on the information given, your return on investment will be:\n\tR{compound_interest_total}')
    breakpoint
    # End of code for investments


# Beginning of code for bonds
elif user_input == 'bond':
# Get user input for the following:
    present_value = int(input("Please enter the current value of your property (numbers only): "))
    interest_rate_bond = float(input("Please enter the annual percentage interest rate (as a number only, without the '%' sign): "))
    months_to_repay = int(input('Please enter the number of months you plan to take to repay the bond: '))

    # Bond repayment formula (from assignment):
    # The amount that a person will have to be repaid on a home loan each
    # month is calculated as follows: repayment = x = (i.P)/(1 - (1+i)^(-n))
    # In the formula above:
    # ● ‘P’ is the present value of the house.
    # ● ‘i’ is the monthly interest rate, calculated by dividing the annual
    # interest rate by 12.
    # ● ‘n’ is the number of months over which the bond will be repaid.
    i = interest_rate_bond / 12
    monthly_repayment = round((i*present_value) / (1 - (1+i)**(-months_to_repay)), 2)

    # Print the amount to repay each month:
    print(f'The amount you need to repay each month is: R{monthly_repayment}')

# End of code






