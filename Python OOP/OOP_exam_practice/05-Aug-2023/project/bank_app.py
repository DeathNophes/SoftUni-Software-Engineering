from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan


class BankApp:
    VALID_LOANS = {
        "StudentLoan": StudentLoan,
        "MortgageLoan": MortgageLoan
    }

    VALID_CLIENTS = {
        "Student": Student,
        "Adult": Adult
    }

    VALID_CLIENTS_LOANS = {
        "Student": "StudentLoan",
        "Adult": "MortgageLoan"
    }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        try:
            loan = self.VALID_LOANS[loan_type]()
        except KeyError:
            raise Exception("Invalid loan type!")

        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        try:
            client = self.VALID_CLIENTS[client_type](client_name, client_id, income)
        except KeyError:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        loans = [l for l in self.loans if loan_type == l.__class__.__name__]
        client = next(filter(lambda c: c.client_id == client_id, self.clients))

        if self.VALID_CLIENTS_LOANS[client.__class__.__name__] != loan_type:
            raise Exception("Inappropriate loan type!")

        index = self.loans.index(loans[0])
        loan = self.loans.pop(index)

        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        try:
            client = next(filter(lambda c: c.client_id == client_id, self.clients))
        except StopIteration:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        loans = [l for l in self.loans if loan_type == l.__class__.__name__]

        for loan in loans:
            loan.increase_interest_rate()

        return f"Successfully changed {len(loans)} loans."

    def increase_clients_interest(self, min_rate: float):
        clients_list = [c for c in self.clients if c.interest < min_rate]

        for client in clients_list:
            client.increase_clients_interest()

        return f"Number of clients affected: {len(clients_list)}."

    def get_statistics(self):
        total_clients_income = sum([c.income for c in self.clients])
        total_loans_granted_to_clients = sum([len(c.loans) for c in self.clients])
        all_loans = [l for c in self.clients for l in c.loans]
        granted_sum = sum([l.amount for l in all_loans])
        not_granted_sum = sum([l.amount for l in self.loans])
        client_interest_rate = sum([c.interest for c in self.clients])
        if client_interest_rate > 0:
            avg_client_interest_rate = client_interest_rate / len(self.clients)
        else:
            avg_client_interest_rate = 0

        return f"Active Clients: {len(self.clients)}\n" + \
               f"Total Income: {total_clients_income:.2f}\n" + \
               f"Granted Loans: {total_loans_granted_to_clients}, Total Sum: {granted_sum:.2f}\n" + \
               f"Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}\n" + \
               f"Average Client Interest Rate: {avg_client_interest_rate:.2f}"
