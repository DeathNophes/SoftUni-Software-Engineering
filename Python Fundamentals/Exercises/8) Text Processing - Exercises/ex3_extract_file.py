file = input().split("\\")
file_name_extension = file[-1].split(".")
print(f"File name: {file_name_extension[0]}")
print(f"File extension: {file_name_extension[1]}")