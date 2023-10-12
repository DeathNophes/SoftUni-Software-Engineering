def password_validator(some_password: str) -> list:
    list_of_errors = ["Password must be between 6 and 10 characters",
                      "Password must consist only of letters and digits",
                      "Password must have at least 2 digits"]
    my_errors = []
    if len(some_password) < 6 or len(some_password) > 10:
        my_errors.append(list_of_errors[0])
    if not some_password.isalnum():
        my_errors.append(list_of_errors[1])
    digits_counter = 0
    for symbol in some_password:
        if symbol.isdigit(): # if True
            digits_counter += 1
    if digits_counter < 2:
        my_errors.append(list_of_errors[2])
    return my_errors


password = input()
errors_in_password = password_validator(password)
if not errors_in_password: # No contents of list (no errors)
    print("Password is valid")
else:
    print(f"\n".join(errors_in_password))