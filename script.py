import numpy as np
print("Enter the Sudoku Grid (Enter 0 for blank spaces).")
grid=[]
for _ in range (0,9):
    a=list(map(int,input().split()))
    grid.append(a)

def check(row, column, number):
    global grid
    for i in range(0,9):
        if grid[row][i] == number:
            return False
    for i in range(0,9):
        if grid[i][column] == number:
            return False
    x=(row//3)*3
    y=(column//3)*3

    for i in range(0,3):
        for j in range(0,3):
            if grid[x+i][y+j]==number:
                return False
    
    return True

def Solve():
    global grid
    for i in range(0,9):
        for j in range(0,9):
            if grid[i][j]==0:
                for number in range(1,10):
                    if check(i,j,number):
                        grid[i][j]=number
                        Solve()
                        grid[i][j]=0
                return

    print(np.matrix(grid))
    input("More Possible solutions")

Solve()
 
