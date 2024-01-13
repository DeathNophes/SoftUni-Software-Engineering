def simple_interest(p, r, t):
    amount = p * r * t
    total_profit = f"${amount:.1f}"
    return total_profit


def complex_interest(p, r, n, t):
    amount = p * (1 + (r / n)) ** (n * t)
    profit = amount - p
    total_profit = f"${profit:.1f}"
    return total_profit


def loan_payments(p, r, t):
    interest = p * r * t
    total_amount = p + interest
    return f"{total_amount:.1f}"


def future_value_of_saving(p, r, n, t):
    amount = p * (1 + (r / n)) ** (n * t)
    total_money = f"${amount:.1f}"
    return total_money


def which_function(some_function: int):
    if some_function == 1:
        operation = "Simple Interest"
        return "Calculate Simple Interest", operation
    elif some_function == 2:
        operation = "Compound Interest"
        return "Calculate Compound Interest", operation
    elif some_function == 3:
        operation = "Loan Payment"
        return "Calculate Loan Payment", operation
    elif some_function == 4:
        operation = "Future Value of Savings"
        return "Calculate Future Value of Savings", operation


def main_menu():
    function = input("Main Menu:\n\n1. Calculate Simple Interest\n2. Calculate Compound Interest\n"
                     "3. Calculate Loan Payments\n4. Calculate Future Value of Savings\n5. Quit\n\n"
                     "Enter your choice(1/2/3/4/5): ")

    if function == "5":
        return "Goodbye"

    if not int(function.isdigit()) or not 1 <= int(function) <= 5:
        return "Error"

    text, operation_name = which_function(int(function))

    principal_amount = input("Enter principal amount: ")
    annual_interest_rate = input("Enter annual interest rate (as a decimal): ")
    num_of_compounds_per_year = input("Enter the number of times interest is compounded per year: ")
    years = input("Enter time (in years): ")

    checking1 = principal_amount.isdigit()
    checking2 = annual_interest_rate.isdigit()
    checking3 = num_of_compounds_per_year.isdigit()
    checking4 = years.isdigit()

    if not checking1 or not checking2 or not checking3 or not checking4:
        return "Wrong input"

    if principal_amount == 0 or annual_interest_rate == 0 or num_of_compounds_per_year == 0 or years == 0:
        return "Error"

    if function == "1":
        profit = simple_interest(int(principal_amount), float(annual_interest_rate), int(years))
        final = f"{operation_name}: {profit}"
        return final

    elif function == "2":
        profit = complex_interest(int(principal_amount), float(annual_interest_rate), int(num_of_compounds_per_year),
                                  int(years))
        final = f"{operation_name}: {profit}"
        return final

    elif function == "3":
        total_money_to_return = loan_payments(int(principal_amount), float(annual_interest_rate), int(years))
        final = f"{operation_name}: {total_money_to_return}"
        return final

    elif function == "4":
        total_money = future_value_of_saving(int(principal_amount), float(annual_interest_rate),
                                             int(num_of_compounds_per_year), int(years))
        final = f"{operation_name}: {total_money}"
        return final


while True:
    result = main_menu()
    if result == "Goodbye":
        print("Goodbye")
        break
    print(result)
    do_you_want_to_continue = input("Do you want to perform another calculation? (yes/no): ")
    if do_you_want_to_continue == 'no':
        break
    elif do_you_want_to_continue == 'yes':
        continue
    else:
        print("Wrong input")
        break
