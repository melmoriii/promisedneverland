"""
    постоянно работающий светофор по умолчанию красным для пешехода
    по нажатию на кнопку запускает механизм перехода на зелёный свет
    (с соответствующими комментариями)
"""
import time

red_seconds = 10
green_seconds = 12
button = False
while True:
    while not button:
        print("red")
        button = input()
    while red_seconds != 0:
        print(f"seconds:{red_seconds}")
        time.sleep(0.5)
        red_seconds -= 1
    print("green")
    print("you can go")
    while green_seconds != 0:
        print(f"seconds:{green_seconds}")
        time.sleep(0.5)
        green_seconds -= 1
    print("stop")
    button = False
    red_seconds = 10
    green_seconds = 12