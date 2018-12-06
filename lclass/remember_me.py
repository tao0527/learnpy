import json


def get_stored_name():
    """如果已存储，直接获取之"""
    filename = "username.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    """welcome back"""
    username = get_stored_name()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = input("What's your name?\n")
        filename = "username.json"
        with open(filename, "w") as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")


greet_user()

# def greet_user1():
#     filename = 'username.json'
#
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj)
#     except FileNotFoundError:
#         username = input("What's your name?\n")
#         with open(filename, "w") as f_obj:
#             json.dump(username, f_obj)
#             print("We'll remember you when you come back, " + username + "!")
#     else:
#         print("Welcome back, " + username + "!")
#
#
# greet_user()
