import random

empty = "0"
num2 = "2"
num4 = "4"
num8 = "8"
num16 = "16"
num32 = "32"
num64 = "64"
num128 = "128"
num256 = "256"
num512 = "512"
num1024 = "1024"
num2048 = "2048"

animal = {
    "0": "🐞",
    "2": '🐶',
    "4": '🐱',
    "8": '🐭',
    "16": '🐹',
    "32": '🐰',
    "64": '🦊',
    "128": '🐻',
    "256": '🐼',
    "512": '🐘',
    "1024": '🐨',
    "2048": '🐷',
}


def prtScreen(screen, score):
    rows = ""
    animal_stile = ""
    for row in screen:
        for item in row:
            animal_stile += animal[item] + " "
            rows = rows + item + " "
        if row:
            rows += "\n"
            animal_stile += "\n"
    return [rows, score, animal_stile]


row1 = 1
row2 = 4
row3 = 7
row4 = 10


def start_game_2048(screen, score, moved, move):
    d = screen.split()
    screen = []
    for i in range(12):
        screen.append([])
    s = [[0, 1, 2, 3],
         [4, 5, 6, 7],
         [8, 9, 10, 11],
         [12, 13, 14, 15]]
    numbers = [1, 4, 7, 10]
    for i in range(4):
        for k in range(4):
            screen[numbers[i]].append(d[s[i][k]])
    if not score:
        score = 0
    else:
        score = score

    numbers = [1, 4, 7, 10]
    randX = random.randint(0, 3)
    randY = random.choice(numbers)
    screen[randY][randX] = num2

    if moved or move:
        randX = random.randint(0, 3)
        randY = random.choice(numbers)
        while screen[randY][randX] != empty:
            randX = random.randint(0, 3)
            randY = random.choice(numbers)

        screen[randY][randX] = num2

    move = False
    moved = False

    return [screen, score, moved, move]


def add_new_field(screen, score, moved, move):
    numbers = [1, 4, 7, 10]
    if moved or move:
        randX = random.randint(0, 3)
        randY = random.choice(numbers)
        while screen[randY][randX] != empty:
            randX = random.randint(0, 3)
            randY = random.choice(numbers)

        screen[randY][randX] = num2

    move = False
    moved = False

    return [screen, score, moved, move]


def key_handler(keypress, screen, score, moved, move):
    d = screen.split()
    screen = []
    for i in range(12):
        screen.append([])
    s = [[0, 1, 2, 3],
         [4, 5, 6, 7],
         [8, 9, 10, 11],
         [12, 13, 14, 15]]
    numbers = [1, 4, 7, 10]
    for i in range(4):
        for k in range(4):
            screen[numbers[i]].append(d[s[i][k]])
    if not score:
        score = 0
    else:
        score = score
    if keypress == "d":
        for loops in range(3):
            for row in [1, 4, 7, 10]:
                for i in range(len(screen[row]) - 2, -1, -1):
                    if screen[row][i + 1] == empty and screen[row][i] != empty:
                        screen[row][i + 1] = screen[row][i]
                        screen[row][i] = empty
                        move = True
                    elif screen[row][i] == screen[row][i + 1]:
                        if screen[row][i] == num2:
                            screen[row][i] = empty
                            screen[row][i + 1] = num4
                            score += 4
                            moved = True
                        elif screen[row][i] == num4:
                            screen[row][i] = empty
                            screen[row][i + 1] = num8
                            score += 8
                            moved = True
                        elif screen[row][i] == num8:
                            screen[row][i] = empty
                            screen[row][i + 1] = num16
                            score += 16
                            moved = True
                        elif screen[row][i] == num16:
                            screen[row][i] = empty
                            screen[row][i + 1] = num32
                            score += 32
                            moved = True
                        elif screen[row][i] == num32:
                            screen[row][i] = empty
                            screen[row][i + 1] = num64
                            score += 64
                            moved = True
                        elif screen[row][i] == num64:
                            screen[row][i] = empty
                            screen[row][i + 1] = num128
                            score += 128
                            moved = True
                        elif screen[row][i] == num128:
                            screen[row][i] = empty
                            screen[row][i + 1] = num256
                            score += 256
                            moved = True
                        elif screen[row][i] == num256:
                            screen[row][i] = empty
                            screen[row][i + 1] = num512
                            score += 512
                            moved = True
                        elif screen[row][i] == num512:
                            screen[row][i] = empty
                            screen[row][i + 1] = num1024
                            score += 1024
                            moved = True
                        elif screen[row][i] == num1024:
                            screen[row][i] = empty
                            screen[row][i + 1] = num2048
                            score += 2048
                            moved = True

    elif keypress == "a":
        for loops in range(3):
            for row in [1, 4, 7, 10]:
                for i in range(1, len(screen[row])):
                    if screen[row][i - 1] == empty and screen[row][i] != empty:
                        screen[row][i - 1] = screen[row][i]
                        screen[row][i] = empty
                        move = True
                    elif screen[row][i] == screen[row][i - 1]:
                        if screen[row][i] == num2:
                            screen[row][i] = empty
                            screen[row][i - 1] = num4
                            score += 4
                            moved = True
                        elif screen[row][i] == num4:
                            screen[row][i] = empty
                            screen[row][i - 1] = num8
                            score += 8
                            moved = True
                        elif screen[row][i] == num8:
                            screen[row][i] = empty
                            screen[row][i - 1] = num16
                            score += 16
                            moved = True
                        elif screen[row][i] == num16:
                            screen[row][i] = empty
                            screen[row][i - 1] = num32
                            score += 32
                            moved = True
                        elif screen[row][i] == num32:
                            screen[row][i] = empty
                            screen[row][i - 1] = num64
                            score += 64
                            moved = True
                        elif screen[row][i] == num64:
                            screen[row][i] = empty
                            screen[row][i - 1] = num128
                            score += 128
                            moved = True
                        elif screen[row][i] == num128:
                            screen[row][i] = empty
                            screen[row][i - 1] = num256
                            score += 256
                            moved = True
                        elif screen[row][i] == num256:
                            screen[row][i] = empty
                            screen[row][i - 1] = num512
                            score += 512
                            moved = True
                        elif screen[row][i] == num512:
                            screen[row][i] = empty
                            screen[row][i - 1] = num1024
                            score += 1024
                            moved = True
                        elif screen[row][i] == num1024:
                            screen[row][i] = empty
                            screen[row][i - 1] = num2048
                            score += 2048
                            moved = True

    elif keypress == "s":
        for loops in range(3):
            for row in [7, 4, 1]:
                moved = False
                for i in range(len(screen[row])):
                    if screen[row + 3][i] == empty and screen[row][i] != empty:
                        screen[row + 3][i] = screen[row][i]
                        screen[row][i] = empty
                        move = True
                    elif screen[row][i] == screen[row + 3][i]:
                        if screen[row][i] == num2:
                            screen[row][i] = empty
                            screen[row + 3][i] = num4
                            score += 4
                            moved = True
                        elif screen[row][i] == num4:
                            screen[row][i] = empty
                            screen[row + 3][i] = num8
                            score += 8
                            moved = True
                        elif screen[row][i] == num8:
                            screen[row][i] = empty
                            screen[row + 3][i] = num16
                            score += 16
                            moved = True
                        elif screen[row][i] == num16:
                            screen[row][i] = empty
                            screen[row + 3][i] = num32
                            score += 32
                            moved = True
                        elif screen[row][i] == num32:
                            screen[row][i] = empty
                            screen[row + 3][i] = num64
                            score += 64
                            moved = True
                        elif screen[row][i] == num64:
                            screen[row][i] = empty
                            screen[row + 3][i] = num128
                            score += 128
                            moved = True
                        elif screen[row][i] == num128:
                            screen[row][i] = empty
                            screen[row + 3][i] = num256
                            score += 256
                            moved = True
                        elif screen[row][i] == num256:
                            screen[row][i] = empty
                            screen[row + 3][i] = num512
                            score += 512
                            moved = True
                        elif screen[row][i] == num512:
                            screen[row][i] = empty
                            screen[row + 3][i] = num1024
                            score += 1025
                            moved = True
                        elif screen[row][i] == num1024:
                            screen[row][i] = empty
                            screen[row + 3][i] = num2048
                            score += 2048
                            moved = True

    elif keypress == "w":
        for loops in range(3):
            for row in [4, 7, 10]:
                moved = False
                for i in range(len(screen[row])):
                    if screen[row - 3][i] == empty and screen[row][i] != empty:
                        screen[row - 3][i] = screen[row][i]
                        screen[row][i] = empty
                        move = True
                    elif screen[row][i] == screen[row - 3][i]:
                        if screen[row][i] == num2:
                            screen[row][i] = empty
                            screen[row - 3][i] = num4
                            score += 4
                            moved = True
                        elif screen[row][i] == num4:
                            screen[row][i] = empty
                            screen[row - 3][i] = num8
                            score += 8
                            moved = True
                        elif screen[row][i] == num8:
                            screen[row][i] = empty
                            screen[row - 3][i] = num16
                            score += 16
                            moved = True
                        elif screen[row][i] == num16:
                            screen[row][i] = empty
                            screen[row - 3][i] = num32
                            score += 32
                            moved = True
                        elif screen[row][i] == num32:
                            screen[row][i] = empty
                            screen[row - 3][i] = num64
                            score += 64
                            moved = True
                        elif screen[row][i] == num64:
                            screen[row][i] = empty
                            screen[row - 3][i] = num128
                            score += 128
                            moved = True
                        elif screen[row][i] == num128:
                            screen[row][i] = empty
                            screen[row - 3][i] = num256
                            score += 256
                            moved = True
                        elif screen[row][i] == num256:
                            screen[row][i] = empty
                            screen[row - 3][i] = num512
                            score += 512
                            moved = True
                        elif screen[row][i] == num512:
                            screen[row][i] = empty
                            screen[row - 3][i] = num1024
                            score += 1024
                            moved = True
                        elif screen[row][i] == num1024:
                            screen[row][i] = empty
                            screen[row - 3][i] = num2048
                            score += 2048
                            moved = True

    return [screen, score, moved, move]


def to_check_win_or_lose(screen):
    for rows in [1, 4, 7, 10]:
        for i in screen[rows]:
            if i == num2048:
                """Win"""
                return "Win"

    spaces = False
    for rows in [1, 4, 7, 10]:
        for i in range(len(screen[rows])):
            if screen[rows][i] == empty:
                spaces = True

    loss = False
    if not spaces:
        loss = True
        for rows in [1, 4, 7, 10]:
            for i in range(len(screen[rows])):
                if rows != 1 and screen[rows][i] == screen[rows - 3][i]:
                    loss = False
                if rows != 10 and screen[rows][i] == screen[rows + 3][i]:
                    loss = False
                if i != 0 and screen[rows][i] == screen[rows][i - 1]:
                    loss = False
                if i != 3 and screen[rows][i] == screen[rows][i + 1]:
                    loss = False

    if loss:
        """Lose"""
        return "Lose"
