game_area = list(range(1, 10))
# print(game_area)


win_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def field_to_play():
    for el in range(3):
        print(game_area[0 + el * 3],  game_area[1 + el * 3],  game_area[2 + el * 3])



def cross_or_toe(token):
    while True:
        elem = print("Select input field:" + token)
        if elem in '123456789':
            elem = int(elem)
            if str(game_area [elem - 1] in "XO"):
                print("The field is occupied =(. Try again =)")
                continue
            else:
                game_area[elem - 1] = token
                break
        else:
            print("Wrong! Try again =)")
            continue




def program_chek():
    for i in win_list:
        for el in i:
            if win_list[i][el] == win_list[i][el + 1] == win_list[i][el + 2]:



def main():
    pass
