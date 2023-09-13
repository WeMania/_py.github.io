import os, sys

move_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
bool_move = "O"
active = True


def interface():
    return  f"""            {move_list[0]} | {move_list[1]} | {move_list[2]}
           ---|---|---
            {move_list[3]} | {move_list[4]} | {move_list[5]}
           ---|---|--- 
            {move_list[6]} | {move_list[7]} | {move_list[8]}"""


def interface_print():
    os.system("clear")
    print(interface())


def valid_move():
    global move
    interface_print()
    try:
        move = int(input("\nEnter Valid Move: "))
    except ValueError:
        valid_move()
    if move > 9:
        valid_move()
    if str(move) not in move_list:
        valid_move()


def main():
    valid_move()
    move_list[move - 1] = bool_move
    interface_print()


def end_game(a, b, c):
    global active
    if a == b and b == c:
        interface()
        print(a + " Won The Game ! ")
        active = False


while True:
    while active:
        bool_move = "X" if bool_move == "O" else "O"
        main()

        end_game(move_list[0], move_list[1], move_list[2])
        end_game(move_list[3], move_list[4], move_list[5])
        end_game(move_list[6], move_list[7], move_list[8])
        end_game(move_list[0], move_list[3], move_list[6])
        end_game(move_list[1], move_list[4], move_list[7])
        end_game(move_list[2], move_list[5], move_list[8])
        end_game(move_list[0], move_list[4], move_list[8])
        end_game(move_list[2], move_list[4], move_list[6])
        
        if move_list.count("X") == 5:
            print("\nIts A Draw !")
            active = False

    while not active:
        ans = input("Type (r) To Restart or (q) to quit! : ")
        if ans.lower() == "r":
            move_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]
            number_of_moves = 0
            bool_move = "O"
            active = True
        elif ans.lower() == "q":
            sys.exit()