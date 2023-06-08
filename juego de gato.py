import random

# Global variables
table = [["___", "___", "___"],
         ["___", "___", "___"],
         ["___", "___", "___"]]

players = ["_X_", "_O_"]

coordinates = [0, 1, 2]

# Functions
def print_Table():
    for row in range(3):
        for column in range(3):
            print(table[row][column], end=" ")
        print()

def alternate_Player(current_player):
    if current_player == players[0]:
        return players[1]
    else:
        return players[0]

def validate_Position(row, column):
    if row >= 0 and row < 3 and column >= 0 and column < 3:
        if table[row][column] == "___":
            return True
    return False

def mark_Position(row, column, current_player):
    if validate_Position(row, column):
        table[row][column] = current_player
        return True
    else:
        return False

def check_Winner():
    for row in range(3):
        if (table[row][0] == table[row][1] and table[row][1] == table[row][2] and table[row][0] != "___"):
            return True
    for column in range(3):
        if (table[0][column] == table[1][column] and table[1][column] == table[2][column] and table[0][column] != "___"):
            return True
    if (table[0][0] == table[1][1] and table[1][1] == table[2][2] and table[0][0] != "___"):
        return True
    if (table[2][0] == table[1][1] and table[1][1] == table[0][2] and table[2][0] != "___"):
        return True
    for row in range(3):
        for column in range(3):
            if (table[row][column] == "___"):
                return False
    return None

def star_Game():
    current_player = random.choice(players)
    finish = False
    while not finish:
        print_Table()
        print("It´s Player´s Turn  ", current_player)
        row = input("Enter The Row (0, 1, 2): ")
        if not row.isdigit():
            print("Enter A Valid Number")
        else:
            row = int(row)
            if not row in coordinates:
                print("Enter A Valid Number")
            else:
                column = input("Enter The Column (0, 1, 2): ")
                if not column.isdigit():
                    print("Enter A Valid Number")
                else:
                    column = int(column)
                    if not column in coordinates:
                        print("Enter A Valid Number")
                         
                if mark_Position(row, column, current_player):
                    if check_Winner() == False:
                         current_player = alternate_Player(current_player)
                    else:
                         finish = True
                         print_Table()
                         print()
                         if check_Winner() == None:
                             print("The Game Is A Tie")
                         else:
                             print(current_player, "Have Won The Game")


if __name__ == "__main__":
    star_Game()
