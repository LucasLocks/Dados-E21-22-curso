# 060j.py
users = {'Hans': 'active', 'Él-Méonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    # if status == 'inactive':
        # del users[user]
        print(user)
        