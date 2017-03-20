"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    incomes = []
    months_worked = int(input("How many months? "))

    for month in range(1, months_worked + 1):
        income = float(input("Enter income for month {} : ".format(months_worked)))
        incomes.append(income)

    print_income(incomes, months_worked)


def print_income(incomes, months_worked):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months_worked + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()