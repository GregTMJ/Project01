#Первая часть кода для привестствия игроков:
def greetings():
    a = input("Напишите букву Y, если хотите начать игру:  ")
    if a == "Y":
        print("")
        print("Мы начинаем игру в крестики-нолики!")
        print("------------------------------------")
        print("       Желаю честной борьбы")
        print("       уважайте друг друга!")
        print("------------------------------------")
        print("x и y являются координатами таблицы")
        print("")

greetings()

def desk_():
    print("  0 1 2")
    for i in range(3):
        row_info = " ".join(desk[i])
        print(i, row_info)

def rules():
    while True:
        coordinations = input("Введите координаты x и y:").split()

        if len(coordinations) != 2:
            print("введите 2 координаты и не больше!")
            continue

        x, y = coordinations

        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите именно числа, а не что-то другое!")
            continue

        x, y = int(x), int(y)

        if x < 0 or y < 0 or x > 2 or y > 2:
            print("Вы в не диапазона игры, попробуйте что-то другое!")
            continue

        if desk[x][y] != " ":
            print("это место уже занято!")

        return x, y

def wining_point():
    win = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
           ((0, 1), (1, 1), (2, 1)),
           ((0, 2), (1, 2), (2, 2)), ((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2)))
    for cords in win:
        check = []
        for c in cords:
            check.append(desk[c[0]][c[1]])
        if check == ["X", "X", "X"]:
            print("Выиграли крестики!")
            return True
        if check == ["0", "0", "0"]:
            print("Выиграли нолики!")
            return True

    return False

desk = [[" "] * 3 for i in range(3)]
count = 0

while True:
    count += 1
    desk_()
    if count % 2 == 1:
        print("Очередь крестиков !")
    else:
        print("Очередь ноликов !")

    x, y = rules()

    if count % 2 == 1:
        desk[x][y] = "X"
    else:
        desk[x][y] = "0"

    if count == 9:
        print("Ничья!")
        break

    if wining_point():
        break



