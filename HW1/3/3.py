class User:
    def __init__(self, username, gender, age, id):
        self.username = username
        self.gender = gender
        self.age = age
        self.id = id


users = []


def find_users(id):
    global users
    founded_users = []
    for user in users:
        if user.id.startswith(id):
            founded_users.append(user)
    founded_users = sorted(founded_users, key=lambda x: x.id)
    return founded_users[:10] if len(founded_users) > 10 else founded_users


find_counter = 1
while True:
    try:
        inp = input().split()
    except EOFError:
        break
    if inp[0] == "Add":
        username = inp[1]
        gender = inp[2]
        age = inp[3]
        id = inp[4]
        new_user = User(username, gender, age, id)
        users.append(new_user)
        result_log = f'User {inp[4]} added successfully'
        print(result_log)

    elif inp[0] == "Find":
        id = inp[1]
        founded_users = find_users(id)
        if founded_users:
            for user in founded_users:
                result_log = f'{find_counter} {user.username} {user.gender} {user.age} {user.id}'
                print(result_log)
        else:
            result_log = f'{find_counter} No user found'
            print(result_log)
        find_counter += 1
    else:
        break
