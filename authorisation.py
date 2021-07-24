from my_srcs import *
if login == correct_login:
    if password == correct_password:
        print("добро пожаловать на плохую вечеринку")
    else:
        print("неверный пароль")
else:
    print("неверный логин")

if login != correct_login:
    print("неверный логин")
else:
    if password != correct_password:
        print("неверный пароль")
    else:
        print("добро пожаловать на плохую вечеринку")
        
# if login == correct_login and password == correct_password:
#     print("добро пожаловать на плохую вечеринку")
# elif login != correct_login and password == correct_password:
#     print("bye gurl")
# elif login == correct_login and password != correct_password:
#     print("bye gurl")
# elif login != correct_login and password != correct_password:
#     print("bye gurl")

# if login == True and password == True:
#     print("добро пожаловать на плохую вечеринку")
# elif login == False and password == True:
#     print("bye gurl")
# elif login == True and password == False:
#     print("bye gurl")
# elif login == False and password == False:
#     print("bye gurl")
