from tkinter import Button, Entry
from canvas import root, frame
from helpers import clean_screen, get_password_hash, is_password_correct, is_free_space_in_reg_form, is_username_free
from json import dump, loads
from buying_page import display_products
import os


def get_users_data():
    info_data = []

    with open(db_file_path, 'r') as users_file:
        for line in users_file:
            info_data.append(loads(line))

    return info_data


def render_entry():
    register_button = Button(
        root,
        text='Register',
        bg='green',     # Background color
        fg='white',     # Font color
        bd=0,
        width=8,
        height=2,
        command=register
    )

    login_button = Button(
        root,
        text='Login',
        bg='blue',
        fg='white',
        bd=0,
        width=8,
        height=2,
        command=login
    )

    frame.create_window(350, 260, window=register_button)
    frame.create_window(350, 305, window=login_button)


def register():
    clean_screen()

    frame.create_text(100, 50, text='First Name:')
    frame.create_text(100, 100, text='Last Name:')
    frame.create_text(100, 150, text='Username:')
    frame.create_text(100, 200, text='Password:')

    frame.create_window(200, 50, window=first_name_box)
    frame.create_window(200, 100, window=last_name_box)
    frame.create_window(200, 150, window=username_box)
    frame.create_window(200, 200, window=password_box)

    register_button = Button(
        root,
        text='Register',
        bg='green',
        fg='white',
        bd=0,
        width=8,
        height=1,
        command=registration
    )

    frame.create_window(310, 200, window=register_button)


def registration():
    info_dict = {
        'First name': first_name_box.get(),
        'Last name': last_name_box.get(),
        'Username': username_box.get(),
        'Password': password_box.get()
    }
    if check_registration(info_dict):
        with open(db_file_path, 'a') as users_file:
            info_dict["Password"] = get_password_hash(info_dict["Password"])
            dump(info_dict, users_file)
            users_file.write("\n")
            display_products()


def check_registration(info_dict):
    frame.delete('error')  # We remove the errors by their tag so that they don't be one over the other

    users_data = get_users_data()

    if all([is_free_space_in_reg_form(info_dict), is_password_correct(info_dict['Password']),
            is_username_free(users_data, info_dict['Username'])]):
        return True
    else:
        return False


def login():
    clean_screen()

    frame.create_text(100, 50, text='Username:')
    frame.create_text(100, 100, text='Password:')

    frame.create_window(200, 50, window=username_box)
    frame.create_window(200, 100, window=password_box)

    frame.create_window(220, 150, window=login_button)


def logging():
    if check_login():
        display_products()
    else:
        frame.create_text(
            200,
            200,
            text='Invalid username or password',
            fill='red',
            tags='error'
        )


def check_login():
    users_data = get_users_data()

    user_username = username_box.get()
    user_password = get_password_hash(password_box.get())

    for user in users_data:
        curr_user_username = user['Username']
        curr_user_password = user['Password']

        if curr_user_username == user_username and curr_user_password == user_password:
            return True

    return False


def change_login_button_state(event):
    info = [username_box.get(), password_box.get()]

    for el in info:
        if not el.strip():  # We have nothing or just a whitespace
            login_button['state'] = 'disabled'
            break
    else:
        login_button['state'] = 'normal'


first_name_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
username_box = Entry(root, bd=0)
password_box = Entry(root, bd=0, show='*')

login_button = Button(
    root,
    width=6,
    height=1,
    text='Login',
    bd=0,
    bg='blue',
    fg='white',
    command=logging
)

login_button['state'] = 'disabled'

db_file_path = os.path.join('db', 'users_information.txt')

root.bind("<KeyRelease>", change_login_button_state)