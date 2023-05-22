import random


def display(board):
    print("  A B C D E F G H")
    print("  ---------------")
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1


def ship_creator(board):
    for ship in range(5):
        ship_row, ship_col = random.randint(0, 7), random.randint(0, 7)
        while board[ship_row][ship_col] == 'X':
            ship_row, ship_col = random.randint(0, 7), random.randint(0, 7)
        board[ship_row][ship_col] = 'X'


def location(lett_to_num):
    row = input("Please enter ship row(1-8): ")
    while row not in '12345678':
        print("Please input valid row number!")
        row = input("Please enter ship row(1-8): ")
    col = input("Please enter ship column(A-H): ").upper()
    while col not in "ABCDEFGH":
        print("Please input valid column!")
        col = input("Please enter ship column(A-H): ").upper()
    return int(row)-1, lett_to_num[col]


def count_hits(board):
    hit = 0
    for row in board:
        for col in row:
            if col == 'X':
                hit += 1
    return hit


def main():
    hidden_board = [[' '] * 8 for _ in range(8)]
    guess_board = [[' '] * 8 for _ in range(8)]

    lett_to_num = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

    ship_creator(hidden_board)
    turns = 10
    while turns > 0:
        print("Welcome to Battleship")
        display(guess_board)
        row, col = location(lett_to_num)
        if guess_board[row][col] == '-':
            print("You already guessed that spot bud!")
        elif hidden_board[row][col] == 'X':
            print("Boom! you got a hit!")
            guess_board[row][col] = 'X'
            turns -= 1
        else:
            print("Blank!, you missed pal!")
            guess_board[row][col] = '-'
            turns -= 1
        if count_hits(guess_board) == 5:
            print("Congrats, you have sunk all the battleships!")
            print("Thanks for playing battleship!")
            break
        print("You have" + str(turns) + " turns left")
        if turns == 0:
            print("Sorry, no more turns remaining Game over!")
            print("Thanks for playing battleship!")
            break


main()
