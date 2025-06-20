list = []
if list:        #将列表用作if的条件表达式，空列表返回false，非空返回true
    print('')
else:
    print('')


users = ['admin', 'Jack', 'David', 'Tom', 'Tony']
for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")

current_users = ['a', 'Jack', 'David', 'Tom', 'Tony', 's']
current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())
new_users = ['a', 'Jac', 'Dave', 'Tom', 'T', 'S']
for user in new_users:
    if user in current_users or user.lower() in current_users_lower:
        print("this name has been used")
    else:
        print("this name is available")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")

