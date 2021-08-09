"""
    постоянно работающий светофор по умолчанию красным для пешехода
    по нажатию на кнопку запускает механизм перехода на зелёный свет
    (с соответствующими комментариями)
"""
button = input("enter the statement")
clicked_bt = "on"
seconds = 10
while True:
    if button != clicked_bt:
        print("red")
        break
    elif button == clicked_bt:
        if seconds == 0:
            print("green")
            print("you can go")
            break
        elif seconds != 0:
            print(f"seconds:{seconds}")
            seconds = seconds - 1