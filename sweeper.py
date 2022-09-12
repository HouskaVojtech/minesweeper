#!/usr/bin/python3

import random
import numpy as np

class Queue:
    def __init__(self):
        self.container = []

    def add (self, element):
        self.container.append(element)

    def pop(self):
        ret_val = self.container[0]
        del self.container[0]
        return ret_val

    def is_empty(self):
        return True if len(self.container) == 0 else False

def coor_sum(t1, t2):
    first = t1[0] + t2[0]
    second = t1[1] + t2[1]
    return (first, second)


class Field:
    def __init__(self, n_rows, n_cols, n_mines):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.field = self.create_empty_field(n_rows, n_cols, n_mines)
        self.count_all()
        self.player_field = self.init_player_field()

    def display_player(self):
        for row in self.player_field:
            for i in row:
                print (i, end="")
            print()

    def display_revealed(self):
        for row in self.field:
            for i in row:
                print (i, end="")
            print()

    def init_player_field(self):
        field = []
        for s in ("#" * self.n_rows * self.n_cols):
            field.append(s)
        return np.reshape(field,(n_rows, n_cols))
        
    def create_empty_field(self, n_rows, n_cols, n_mines):
        string = ("_" * (n_rows * n_cols - n_mines)) + ("*"* n_mines)
        field = []

        for s in string:
            field.append(s)

        random.shuffle(field)

        return np.reshape(field, (n_rows, n_cols))

    def count_all(self):
        for i in range(self.field.shape[0]):
            for j in range(self.field.shape[1]):
                self.field[i][j] = self.check_surroundings(i, j)
        

    def check_surroundings(self, row, col):
        if self.field.shape[0] < row < 0:
            print ( "invalid input" )

        if self.field.shape[1] < col < 0:
            print ( "invalid input" )

        if self.field[row][col] == "*":
            return "*"

        # TODO: use for loops instead of these horendous ifs
#        helper_nums = [-1, 0, 1]
#        for i in helper_nums:
#            for j in helper_nums:
#                if i or j:
#                    surroundings += self.field[row + i]

        surroundings = ""
        if row - 1 >= 0 and col - 1 >= 0:
            surroundings += self.field[row - 1][ col -1]

        if row - 1 >= 0:
            surroundings += self.field[ row - 1][ col ]

        if row - 1 >= 0 and col + 1 < self.field.shape[1]:
            surroundings += self.field[row - 1][ col + 1]

        if col - 1 >= 0:
            surroundings += self.field[row][col -1]

        if col + 1 < self.field.shape[1]:
            surroundings += self.field[row][col +1]

        if row + 1 < self.field.shape[0] and col - 1 >= 0:
            surroundings += self.field[row + 1][ col -1]

        if row + 1 < self.field.shape[0]:
            surroundings += self.field[row + 1][ col ]

        if row + 1 < self.field.shape[0] and col + 1 < self.field.shape[1]:
            surroundings += self.field[row + 1][ col +1]

        cnt = surroundings.count('*') 
        return " " if cnt == 0 else cnt

    def click(self, row, column):
        if self.field[row][column] == '*':
            print('Game Over')
            quit() 

    def is_mine(self,coordinates):
        ...

    def is_number(self,coordinates):
        return self.field[coordinates[0]][coordinates[1]].isnumeric()

    def is_blank(self, coordinates):
        return self.field[coordinates[0]][coordinates[1]] == " "

    def is_valid_coor(self, coordinates):
        if coordinates[0] < 0 or coordinates[1] < 0:
            return False
        if coordinates[0] >= self.n_rows or coordinates[1] >= self.n_cols:
            return False
        return True

    def neighbors(self, coordinates):
        #TODO: there is a problem that it neighbors does not reveal numbers
        neighbors = []
        helper_nums = [-1, 0, 1]
        for i in helper_nums:
            for j in helper_nums:
                if i or j:
                    adjacent = coor_sum(coordinates, (i, j))
                    if self.is_blank(adjacent) or (self.is_blank(coordinates) and self.is_number(adjacent)):
                        neighbors.append(adjacent)
        return neighbors
        

    def bfs(self, row, column):
        q = Queue()
        self.player_field[row][column] = self.field[row][column]
        beginning = (row, column)
        q.add(beginning)
        while not q.is_empty():
            v = q.pop()
            for w in self.neighbors(v):
                if self.player_field[w[0]][w[1]] != self.field[w[0]][w[1]]:
                    self.player_field[w[0]][w[1]] = self.field[w[0]][w[1]]
                    q.add(w)

    
# BFS
# define Queue q
# lable root as explored
# Q.add(root)
# while q is not empty:
#   v = q.pop()
#   for w in neighbors
#   if w is not explored:
#       lable it as explored
#       q.add(w)

# if I click on a mine game is over
# if I click on a number only a number is revelad


    

if __name__ == '__main__':
    n_rows = 10
    n_cols = 10
    n_mines = 5
    f = Field(n_rows,n_cols, n_mines)
    f.display_player()
    print("-" * 50)
    f.display_revealed()
    #print(create_empty_field(n_rows,n_cols, n_mines))

    print("row")
    row = int(input())
    print("column")
    column = int(input())

    f.bfs(row, column)
    f.display_player()
    print("-" * 50)
    f.display_revealed()
