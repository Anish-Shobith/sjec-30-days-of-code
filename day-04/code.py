def fill(m, n):
    if m % 3 == 0 and n % 3 == 0:
        return True
    if m % 3 == 0 and n % 2 == 0:
        return True
    if m % 2 == 0 and n % 3 == 0:
        return True
    return False

print('Yes' if fill(int(input()), int(input())) else 'No')

