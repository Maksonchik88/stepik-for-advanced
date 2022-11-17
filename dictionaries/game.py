game_area = list(range(1, 10))
# print(game_area)


win_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def field_to_play():
    for el in range(3):
        print(game_area[0 + el * 3], game_area[1 + el * 3], game_area[2 + el * 3])


def cross_or_toe(token):
    while True:
        elem = input("Select input field:" + token + "?")
        if not (elem in '123456789'):
            print("Error. Try again =)")
            continue
        elem = int(elem)
        if str(win_list[elem - 1]) in "XO":
            print("The field is occupied =(. Try again =)")
            continue


def program_chek():
    for el in win_list:
        if win_list[el[0] - 1] == win_list[el[1] - 1 == win_list[el[2] - 1]]:
            return win_list[el[1] - 1]
    else:
        return False


def main():
    counter = 0
    while True:
        field_to_play()
        if counter % 2 == 0:
            cross_or_toe('X')
        else:
            cross_or_toe('O')
            if counter > 3:
                winner = program_chek()
                if winner:
                    field_to_play()
                    print(winner, "win!")
                    break
            else:
                counter += 1
                if counter > 8:
                    field_to_play()
                    print("Draw =)")
                    break


main()
