file_name = 'test.txt'

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())
