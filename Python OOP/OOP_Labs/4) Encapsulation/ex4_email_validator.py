class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails          # List
        self.domains = domains      # List

    def __is_name_valid(self, username):
        return len(username) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        username, data = email.split('@')
        mail, domain = data.split('.')

        result = [
            self.__is_name_valid(username),
            self.__is_mail_valid(mail),
            self.__is_domain_valid(domain)
        ]

        return all(result)
