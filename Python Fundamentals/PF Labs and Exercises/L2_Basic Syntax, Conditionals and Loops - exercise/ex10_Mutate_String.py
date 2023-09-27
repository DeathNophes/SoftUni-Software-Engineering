first_string = input()
second_string = input()
last_printed_string = first_string
for index in range(len(first_string)):
    # Не слагаме +1 за да не ни гръмне програмата
    left_part = second_string[:index + 1]   # От началото до index + 1
    right_part = first_string[index + 1:]   # От index + 1 до края
    # Разглобяваме стринговете на лява и дясна част
    new_string = left_part + right_part
    if new_string != last_printed_string:
        # Принтираме само стринговете, които не се повтарят (уникални)
        print(new_string)
        last_printed_string = new_string
