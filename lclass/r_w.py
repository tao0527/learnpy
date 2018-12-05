import json


file_name = 'test.txt'

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())


username = input("What is your name?\n")

file_name1 = 'username.json'
with open(file_name1, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")
