class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not 5 <= len(value) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")

        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value: str):
        is_valid_length = len(value) >= 8
        is_uppercase_present = len([el for el in value if el.isupper()]) > 0
        is_digit_present = len([el for el in value if el.isdigit()]) > 0

        result = [is_valid_length, is_uppercase_present, is_digit_present]

        if not all(result):
            raise ValueError("The password must be 8 or more characters "
                             "with at least 1 digit and 1 uppercase letter.")

        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'
