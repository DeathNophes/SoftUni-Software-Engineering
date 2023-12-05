tour_stops = input()

command = input()
while command != 'Travel':
    command = command.split(':')
    if 'Add Stop' in command:
        index = int(command[1])
        string = command[2]
        if 0 <= index < len(tour_stops):
            tour_stops = tour_stops[:index] + string + tour_stops[index:]

    elif 'Remove Stop' in command:
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(tour_stops) and \
                0 <= end_index < len(tour_stops):
            tour_stops = tour_stops[:start_index] + tour_stops[end_index + 1:]

    elif 'Switch' in command:
        old_string = command[1]
        new_string = command[2]
        if old_string in tour_stops:
            tour_stops = tour_stops.replace(old_string, new_string)

    print(tour_stops)
    command = input()

print(f"Ready for world tour! Planned stops: {tour_stops}")
