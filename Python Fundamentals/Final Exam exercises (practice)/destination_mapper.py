import re

text = input()
pattern = r'(=|\/)([A-Z]{1}[A-Za-z]{2,})\1'
destinations = []
travel_points = 0
places = re.findall(pattern, text)
for place in places:
    destinations.append(place[1])
    travel_points += len(place[1])
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
