def int_to_binary(number: int):
    if number == 0: return "0"
    bin = ""
    while number:
        bin = str(number%2) + bin
        number //= 2
    return bin

def string_to_binary(text: str) -> str:
    bin = ""
    for c in text:
        n = int_to_binary(ord(c)-65)
        bin += "0"*(5-len(n)) + n
    return bin

def binary_to_string(bitsstring: str) -> str:
    st = ""
    for i in range(0,len(bitsstring),5):
        x = bitsstring[i:i+5]
        while x and x[0] == "0":
            x = x[1:] if len(x) else "0"
        n = 0
        for d in x:
            n = n*2 + int(d)
        st += chr(n+65)
    return st

def string_to_binary_optimized(text: str, letter_freq: list[str]):
    bin = ""
    for c in text:
        if c in letter_freq:
            bin += "0" + ["00","01","10","11"][letter_freq.index(c)]
        else:
            n = int_to_binary(ord(c) - 65)
            bin += "1" + "0" * (5 - len(n)) + n
    return bin

def print_horizontal_bar_chart(numbers):
    for n in numbers:
        print("x "*n + str(n))

def print_vertical_bar_chart(numbers):
    height = max(numbers)
    for lvl in range(height,0,-1):
        for num in numbers:
            if num == lvl-1:
                print(num,end="")
            elif num > lvl-1:
                print("x",end="")
            else: print(" ",end="")
        print()

def flood_fill(image,start_x,start_y):
    image[start_y][start_x] = "."
    for x,y in (0,1),(0,-1),(1,0),(-1,0):
        nx = x+start_x
        ny = y+start_y
        if image[ny][nx] == " ":
            flood_fill(image,nx,ny)

def sum_iterative(numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum

def sum_recursive(numbers):
    if not numbers:
        return 0
    return numbers[0] + sum_recursive(numbers[1:])

def kgV(n,m):
    x = min(n,m)
    while x%n or x%m:
        x += 1
    return x

def add_umlaut(text):
    out = ""
    repl = {"a":"ä","o":"ö","u":"ü","A":"Ä","O":"Ö","U":"Ü"}
    counter = 0
    for chr in text:
        if chr == " ":
            counter = 0
        if chr in repl:
            counter += 1
            if counter == 2:
                out += repl[chr]
                continue
        out += chr
    return out

def print_triangle(n):
    for x in range(-n+1,n):
        print("  "*(abs(x)) + "x "*(n-abs(x)))

def print_circle(n):
    for y in range(-n+1, n):
        for x in range(-n+1, n):
            print("x " if x**2 + y**2 <= n**2 else "  ", end="")
        print()

def print_pacman(n):
    out = []
    for y in range(-n+1, n):
        row = []
        for x in range(-n+1, n):
            row.append("x" if x**2 + y**2 < n**2 else " ")
        for x in range(n-abs(y)):
            row[-x-1] = " "
        out.append(row)
    for row in out:
        print(*row, sep="  ")

def knapsack(weights,max_weight) -> list[int]:
    comb = [[]]
    for i in range(len(weights)):
        comb += [c + [i] for c in comb]
    maxi = []
    maxn = 0
    for c in comb:
        sum = 0
        for i in c:
            sum += weights[i]
        if sum <= max_weight and sum > maxn:
            maxi = c
            maxn = sum
    return maxi

print_triangle(5)