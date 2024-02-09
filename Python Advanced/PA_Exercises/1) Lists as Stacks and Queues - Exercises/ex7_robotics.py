from collections import deque


def read_robots():
    robots_dict = {}
    robot_info = [x.split('-') for x in input().split(';')]
    for robot in robot_info:
        name = robot[0]
        robot_time = int(robot[1])
        robots_dict[name] = robot_time
    return robots_dict


def convert_initial_time_into_seconds(hours, mins, secs):
    return hours * 60 * 60 + mins * 60 + secs


def read_products():
    queue = deque()
    line = input()
    while line != 'End':
        queue.append(line)
        line = input()
    return queue


def convert_to_needed_format_of_time(seconds_of_time):
    hour = seconds_of_time // 3600
    minutes = (seconds_of_time % 3600) // 60
    seconds = (seconds_of_time % 3600) % 60
    return f'{hour:02d}:{minutes:02d}:{seconds:02d}'


robots = read_robots()
available_robots = [k for k in robots.keys()]
dict_with_processing_robots = {}
time_parts = [int(p) for p in input().split(':')]
time_in_seconds = convert_initial_time_into_seconds(time_parts[0], time_parts[1], time_parts[2])
queue_of_products = read_products()

while queue_of_products:
    time_in_seconds = (time_in_seconds + 1) % (24 * 60 * 60)
    for robot_name in [k for k in dict_with_processing_robots.keys()]:
        dict_with_processing_robots[robot_name] -= 1
        if dict_with_processing_robots[robot_name] <= 0:
            dict_with_processing_robots.pop(robot_name)
    current_product = queue_of_products.popleft()
    for robot_name in available_robots:
        if robot_name not in dict_with_processing_robots:
            print(f'{robot_name} - {current_product} [{convert_to_needed_format_of_time(time_in_seconds)}]')
            dict_with_processing_robots[robot_name] = robots[robot_name]
            break
    else:
        queue_of_products.append(current_product)
