import os

report_file_path = os.path.join("files_2", "report.txt")


def save_extensions(dir_name):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)

        if os.path.isfile(file):
            extension = filename.split('.')[-1]

            if extension not in extensions:
                extensions[extension] = []

            extensions[extension].append(filename)

        elif os.path.isdir(filename):
            save_extensions(file)


directory = input()
extensions = {}    # {'py': ['program.py', 'hello.py'], ...}
save_extensions(directory)

sorted_extensions = sorted(extensions.items(), key=lambda x: x[0])
with open(report_file_path, 'w') as report_file:
    report_file.seek(0)
    report_file.truncate()

for curr_extension, names in sorted_extensions:
    with open(report_file_path, 'a') as report_file:
        report_file.write(f".{curr_extension}\n")
        for name in sorted(names):
            if name != 'report.txt':
                report_file.write(f"- - - {name}\n")
