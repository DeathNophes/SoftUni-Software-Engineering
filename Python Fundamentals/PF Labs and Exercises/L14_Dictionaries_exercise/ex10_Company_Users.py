company_users = {}

while True:
    command = input()
    if command == 'End':
        break
    company, employee_id = command.split(" -> ")

    if company not in company_users:
        company_users[company] = [employee_id]
    else:
        if employee_id not in company_users[company]:
            company_users[company].append(employee_id)

for curr_company in company_users.keys():
    print(curr_company)
    for employee in company_users[curr_company]:
        print(f"-- {employee}")
