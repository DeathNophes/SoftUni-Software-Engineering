import os

path = os.path.join('resources', 'my_first_file.txt')
with open(path, 'a') as file:
    file.write('I just created my first file!')

# The file was created in the resources directory
