from my_srcs import *
# if entered_login == login:
#     if entered_password == password:
#         print("добро пожаловать на плохую вечеринку")
#     else:
#         print("неверный пароль")
# else:
#     print("неверный логин")

if entered_login == login:
    if entered_password == password:
        print("welcome")
    else:
        print("wrong password")
        while tries != 0:
            print(f"tries left:{tries}")
            tries = tries - 1
            entered_password = password
else:
    print("wrong login")
# if login != correct_login:
#     print("неверный логин")
# else:
#     if password != correct_password:
#         print("неверный пароль")
#     else:
#         print("добро пожаловать на плохую вечеринку")