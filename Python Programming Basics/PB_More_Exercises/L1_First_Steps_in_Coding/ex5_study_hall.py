w = float(input())
h = float(input())

w_sm = w * 100
h_sm = h * 100
# we turn it all in centimeters
h_sm = h_sm - 100
# we remove 100sm for the corridor
desks_per_row = h_sm // 70
rows = w_sm // 120

all_seats = (desks_per_row * rows) - 3
print(all_seats)