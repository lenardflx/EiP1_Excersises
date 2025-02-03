sudoku = [[0, 0, 2, 0, 0, 0, 9, 0, 0],
          [0, 0, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 7, 5, 0, 0, 4],
          [0, 9, 4, 2, 0, 0, 8, 0, 0],
          [0, 2, 0, 0, 4, 9, 0, 5, 0],
          [7, 0, 3, 0, 1, 0, 0, 0, 0],
          [0, 0, 8, 1, 9, 0, 4, 0, 0],
          [6, 0, 0, 0, 0, 4, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 6],]

def backtracking(sudoku):
    gutes_ding = nächstes_freies_feld(sudoku)
    if gutes_ding is None:
        return True
    reihe, spalte = gutes_ding
    for zahl in range(1, 10):
        if sudoku_regeln(sudoku, reihe, spalte, zahl):
            sudoku[reihe][spalte] = zahl
            gelöst = backtracking(sudoku)
            if gelöst:
                return True
            sudoku[reihe][spalte] = 0
    return False

def print_sudoku(sudoku): #sudoku ausgeben
    print('-' * 25)
    for reihe in range(9):
        if reihe%3 == 0 and reihe != 0:
            print('-' * 25)
        print('|', end=' ')
        for spalte in range(9):
            if spalte%3 == 0 and spalte != 0:
                print('|', end=' ')
            print(sudoku[reihe][spalte], end=' ')
        print('|')
    print('-' * 25)

def nächstes_freies_feld(sudoku): #nächstes nuller-feld suchen / checken ob sudoku gelöst wurde
    for reihe in range(9):
        for spalte in range(9):
            if sudoku[reihe][spalte] == 0:
                return (reihe, spalte)
    return None

def sudoku_regeln(sudoku, reihe, spalte, zahl):
    #reihen-regel
    for i in range(9):
        if sudoku[reihe][i] == zahl:
            return False
    #spalten-regel
    for i in range(9):
        if sudoku[i][spalte] == zahl:
            return False
    #3x3-regel
    box_start_reihe = (reihe // 3) * 3
    box_start_spalte = (spalte // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[box_start_reihe + 1][box_start_spalte + j] == zahl:
                return False
    return True

backtracking(sudoku)
print_sudoku(sudoku)