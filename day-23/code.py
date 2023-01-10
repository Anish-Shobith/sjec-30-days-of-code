def f(n):
    for i in range(500):
        n += int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            return n
    return "NA"

print(f(int(input())))