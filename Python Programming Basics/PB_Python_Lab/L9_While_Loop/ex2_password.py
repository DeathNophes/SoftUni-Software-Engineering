#username = input()
#user_password = input()
#current_password = input()

#while current_password != user_password:
#    current_password = input()
#else:
#    print(f"Welcome {username}!")

username = input()
user_password = input()

while True:
    current_password = input()
    if current_password == user_password:
        print(f"Welcome {username}!")
        break
