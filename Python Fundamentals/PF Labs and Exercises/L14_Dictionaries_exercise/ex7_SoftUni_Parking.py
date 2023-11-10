parking = {}
n = int(input())

for _ in range(n):
    command = input().split()
    username = command[1]
    if 'register' in command:
        license_plate_number = command[2]
        if username not in parking.keys():
            parking[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")

    elif 'unregister' in command:
        if username not in parking.keys():
            print(f"ERROR: user {username} not found")
        else:
            parking.pop(username)
            print(f"{username} unregistered successfully")

for name, plate in parking.items():
    print(f"{name} => {plate}")
