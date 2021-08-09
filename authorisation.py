from my_srcs import *
if entered_login == login:
    entered_password = input("введите пароль")
    while True:
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