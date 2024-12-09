# 1)
def get_roman_number(n):
    if not (0 < n < 11):
        return None
    roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
    return roman_numerals[n - 1]

def sum_roman(x, y):
    res = x + y
    if all(1 <= value <= 10 for value in (x, y, res)):
        return get_roman_number(res)
    return "Fehler"

# 2)
def trib(n):
    if n == 1 or n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        return trib(n - 1) + trib(n - 2) + trib(n - 3)

# 3)
def search_max1(lst):
    if len(lst) == 1:
        return lst[0]
    other_max = search_max1(lst[1:])
    return other_max if lst[0] < other_max else lst[0]
# ohne List Slicing aber mit Hilfsfunktion
def search_max2(lst):
    last_i = len(lst)
    def rec(i, curr_max):
        if i == last_i:
            return curr_max
        if lst[i] > curr_max:
            curr_max = lst[i]
        return rec(i+1, curr_max)
    return rec(0, lst[0])

# Tests
print("\nAufgabe 1:")
print(f"sum_roman(2, 4) = {sum_roman(2, 4)}")
print(f"sum_roman(12, 3) = {sum_roman(12, 3)}")
print(f"sum_roman(5, 6) = {sum_roman(5, 6)}")

print("\nAufgabe 2:")
print(f"trib(3) = {trib(3)}")
print(f"trib(12) = {trib(12)}")
print(f"trib(20) = {trib(20)}")

print("\nAufgabe 3:")
print(f"search_max1([1, 2, 4, 3, 4]) = {search_max1([1, 2, 4, 3, 4])}")
print(f"search_max2([91, 3, 34, 23, 5, 71]) = {search_max2([91, 3, 34, 23, 5, 71])}")