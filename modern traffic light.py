"""
    постоянно работающий светофор по умолчанию красным для пешехода
    по нажатию на кнопку запускает механизм перехода на зелёный свет
    (с соответствующими комментариями)
"""
# import time
# red_seconds = 10
# green_seconds = 12
# button = False
# while True:
#     if button == "on":
#         if red_seconds == 0:
#             print("green")
#             print("you can go")
#             print(f"seconds:{red_seconds}")
#             time.sleep(0.5)
#             red_seconds = red_seconds - 1
#             if green_seconds == 0:
#                 button = False
#                 print("stop")
#         else:
#             print(f"seconds:{red_seconds}")
#             time.sleep(0.5)
#             red_seconds = red_seconds - 1
#     else:
#         print("red")
#         button = input()
import time
red_seconds = 10
green_seconds = 12
button = False
while True:
    if button == False:
        print("red")
        button = input()
    elif button == "on":
        print(f"seconds:{green_seconds}")
        time.sleep(0.5)
        green_seconds -= 1
    else:
        print("green")
        print("you can go")
        if green_seconds != 0:
            print(f"seconds:{red_seconds}")
            time.sleep(0.5)
            red_seconds -= 1
        else:
            print("stop")