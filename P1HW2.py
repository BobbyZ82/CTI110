# CTI 110
# P1HW2 - Expenses
# Zapatar
# 11/3

# input: three expenses, the budget
# processing: total to expenses, compare with budget
# output: did you go over or under

# our variables - type float, because of the decimal place
gas = 0.00
food = 0.00
hotel = 0.00
totalexpenses = 0.00
budget = 0.00
destination = ""

print("this program calculates and displays travel expenses")

print("Enter your budget: ")
budget = float(input())

destination = input("Where are you heading?")

print("GREAT!, Let's total your expenses.")
print("Gas: $")
gas = float(input())

print("Hotel: $")
hotel = float(input())

print("Food: $")
food = float(input())

# add everything up
totalexpenses = gas + hotel + food

print("totalexpenses: $", totalexpenses)
 
# output - did they go over budget?
print("Your total expenses are: $", totalexpenses)
print("Your budget was: $", budget)
if totalexpenses > budget:
    print("You went over budget!")
    print("by: $", totalexpenses - budget)
else:
    print("You stayed within you budget.")
    print("money left: $", budget - totalexpenses)

goAgain = input("Run again? y/n")
if goAgain == "y":
    main()
else:
    print("Goodbye.")

# start the program
main()
