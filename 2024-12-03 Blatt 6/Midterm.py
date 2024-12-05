# 1)
def get_roman_number(n):
    return ["I","II","III","IV","V","VI","VII","VIII","IX","X"][n-1] if 0 < n < 11 else None
def sum_roman(x, y):
    return get_roman_number(x + y) if 0 < x < 11 and 0 < y < 11 and (x + y) <= 10 else "Fehler"
# 2)
def trib(n):
    return 1 if n in [1,2] else 2 if n == 3 else trib(n-1) + trib(n-2) + trib(n-3)
# 3)
def search_max(lst):
    return lst[0] if len(lst) == 1 or lst[0] > (m := search_max(lst[1:])) else m
# Tests
tests = [[sum_roman,[[2,4],[12,3],[5,6]]],[trib,[[1],[3],[12],[20]]],[search_max,[[[1,2,3,4]],[[91,3,34,23,5,71]]]]]
for n, (f, t) in enumerate(tests,1):
    print(f"\nAufgabe {n}:\n" + "\n".join(f"{f.__name__}{tuple(arg)} = {f(*arg)}" for arg in t))