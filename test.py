# name1 = "line"
# name2 = "longline"
# name3 = "biglongline"
# street = [name1, name2]
# street.append(name3)
# print(street)
# victim = street[-1]
# print(victim)
# street[0] = "newline"
# print(street)
# street[-1] = "verybiglongline"
# print(street)
# contact = ("+380970979665", "name1")
# print(contact[1])
# print(type(street), type(contact))
# print(dir(street))
# print(dir(contact))

# name = 'melissa'
# age = 16
# test = f"my name is {name} and i'm {age+1}"
# print(test)
# print(type(test))
# test2 = "my name is " + name + " and i'm " + str(age+1)
# print(test2)
# print(type(test2))

# if False:
#     print("it works")
# else:
#     print("it doesn't work")
# print()
# import this
# x = input()
# print(f"{x}\n"*100)

# password = "qwerty"
# enter = input()
# tries = 2
# while True:
#     if enter == password:
#         print("welcome")
#         break
#     elif tries == 0:
#         print("go away")
#         break
#     else:
#         print(f"tries left:{tries}")
#         tries = tries - 1
#         enter = input()

# x = 10
# while x > 0:
#     print("cycle works")
#     print("cycle still works")
# print(3 == 3)
# x = bool("")
# print(x)
print(["раскольников", "старуха-процентщица", "разумихин"])
chars = ["раскольников", "старуха-процентщица", "разумихин"]
# print(len(chars))
# while chars:
#     print(chars[0])
#     del chars[0]

for i in chars:
    print(i)

while True:   #same result via while with no kills (use len for help)
    pass
