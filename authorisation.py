from my_srcs import *
# if entered_login == login:
#     if entered_password == password:
#         print("добро пожаловать на плохую вечеринку")
#     else:
#         print("неверный пароль")
# else:
#     print("неверный логин")
while True:
    if entered_login == login:
        entered_password = input("введите пароль")
        if entered_password == password:
            print("welcome")
            break
        elif tries == 0:
            print("go away")
            break
        else:
            print(f"tries left:{tries}")
            tries = tries - 1
            entered_password = input("введите пароль")
    else:
        print("wrong login")

# if login != correct_login:
#     print("неверный логин")
# else:
#     if password != correct_password:
#         print("неверный пароль")
#     else:
#         print("добро пожаловать на плохую вечеринку")