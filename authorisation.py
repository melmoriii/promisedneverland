from my_srcs import login, loginr, password, passwordr
if login == loginr and password == passwordr:
    print("добро пожаловать на плохую вечеринку")
elif login != loginr and password == passwordr:
    print("bye gurl")
elif login == loginr and password != passwordr:
    print("bye gurl")
elif login != loginr and password != passwordr:
    print("bye gurl")

# if login == True and password == True:
#     print("добро пожаловать на плохую вечеринку")
# elif login == False and password == True:
#     print("bye gurl")
# elif login == True and password == False:
#     print("bye gurl")
# elif login == False and password == False:
#     print("bye gurl")