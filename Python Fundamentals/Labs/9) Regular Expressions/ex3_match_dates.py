import re

dates = input()
regex = r'\b\d{2}/[A-Z][a-z]{2}/\d{4}|\b\d{2}-[A-Z][a-z]{2}-\d{4}|\b\d{2}\.[A-Z][a-z]{2}.\d{4}\b'

matches = re.findall(regex, dates)
valid_dates = [match for match in matches]

for date in valid_dates:
    if '/' in date:
        curr_date = date.split('/')
        print(f"Day: {curr_date[0]}, Month: {curr_date[1]}, Year: {curr_date[2]}")
    elif '-' in date:
        curr_date = date.split('-')
        print(f"Day: {curr_date[0]}, Month: {curr_date[1]}, Year: {curr_date[2]}")
    elif '.' in date:
        curr_date = date.split('.')
        print(f"Day: {curr_date[0]}, Month: {curr_date[1]}, Year: {curr_date[2]}")
