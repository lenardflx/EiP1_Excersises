import random

def _can_place(x, y, n, mat):
    if n in mat[y] or n in [mat[i][x] for i in range(9)]:
        return False
    r,c = (y//3)*3,(x//3)*3
    return all(mat[r+i][c+j] != n for i in range(3) for j in range(3))

def _solve(mat,pos,sample_items=False):
    y,x = pos//9,pos%9
    if y == 9:
        return True
    if mat[y][x] != 0:
        return _solve(mat, pos + 1)
    numbers = random.sample(range(1,10),9) if sample_items else range(1,10)
    for n in numbers:
        if _can_place(x, y, n, mat):
            mat[y][x] = n
            if _solve(mat, pos + 1):
                return True
    mat[y][x] = 0
    return False

def solve_sudoku(mat):
    mat = [r[:] for r in mat]
    _solve(mat, 0)
    return mat

def _count_solutions(mat, pos=0):
    if pos == 81:
        return 1
    y, x = divmod(pos, 9)
    if mat[y][x]:
        return _count_solutions(mat, pos + 1)
    count = 0
    for n in range(1, 10):
        if _can_place(x, y, n, mat):
            mat[y][x] = n
            count += _count_solutions(mat, pos + 1)
            if count > 1:
                break
            mat[y][x] = 0
    mat[y][x] = 0
    return count

def generate_sudoku(difficulty=40):
    orig = [[0] * 9 for _ in range(9)]
    _solve(orig, 0, sample_items=True)
    mat = [row[:] for row in orig]
    cells = [(y, x) for y in range(9) for x in range(9)]
    random.shuffle(cells)
    removed = 0
    for y, x in cells:
        if removed >= difficulty:
            break
        temp = mat[y][x]
        mat[y][x] = 0
        if _count_solutions([row[:] for row in mat]) != 1:
            mat[y][x] = temp
        else:
            removed += 1
    return mat, orig

def check_sudoku(mat):
    right = set(range(1, 10))
    for i in range(9):
        if set(mat[i]) != right or set(mat[j][i] for j in range(9)) != right:
            return False
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            box = {mat[r + i][c + j] for i in range(3) for j in range(3)}
            if box != right:
                return False
    return True

def print_sudoku(mat):
    print("+-------+-------+-------+")
    for i, row in enumerate(mat):
        print("|", end=" ")
        for j, num in enumerate(row):
            print(num if num else " ", end=" ")
            if j % 3 == 2:
                print("|", end=" ")
        print()
        if i % 3 == 2:
            print("+-------+-------+-------+")

maze = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
       ]

maze, orig = generate_sudoku(60)
solved_maze = solve_sudoku(maze)
print_sudoku(maze)
print_sudoku(solved_maze)
print(f"\nSolved: {"✅" if check_sudoku(solved_maze) else "❌"}")
