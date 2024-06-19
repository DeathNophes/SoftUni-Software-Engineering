import os

file_name = "text.txt"
path = os.path.join("resources", file_name)

try:
    file = open(path)
    print("File found")
except FileNotFoundError:
    print("File is not found")
