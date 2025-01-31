def check_b_in_a(a, b):
    for i in b:
        for j in a:
            if i == j:
                break
        else:
            return False
    return True

a = [1, 2, 3]
b = [2, 3]
print(check_b_in_a(a, b))  # True