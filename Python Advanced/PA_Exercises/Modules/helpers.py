from canvas import frame
from hashlib import sha256
import re


def clean_screen():
    frame.delete('all')


def get_password_hash(password):
    hash_object = sha256(password.encode("UTF-8"))
    return hash_object.hexdigest()


def is_free_space_in_reg_form(info_dict):
    for key, value in info_dict.items():
        if not value.strip():
            frame.create_text(
                300,
                300,
                text=f"{key} cannot be empty!",
                fill='red',
                tags='error'
            )
            return False
    return True


def is_username_free(data, username):
    for user in data:
        if user['Username'] == username:
            frame.create_text(
                300,
                320,
                text='Username is already taken',
                fill='red',
                tags='error'
            )
            return False
    return True


def is_password_correct(password):
    password_pattern = r'^[0-9A-Za-z!@#$%^&*_|><]{6,16}$'
    if not re.match(password_pattern, password):
        frame.create_text(
            320,
            340,
            text='Password must be between 6 and 16 digits and must contain only letters,'
                 ' numbers and special symbols',
            fill='red',
            tags='error'
        )
        return False
    return True
