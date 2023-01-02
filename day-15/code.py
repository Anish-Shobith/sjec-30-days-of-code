numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

roman = input()[::-1]
result = 0
for i, r in enumerate(roman):
    if i > 0 and numerals[r] < numerals[roman[i - 1]]:
        result -= numerals[r]
    else:
        result += numerals[r]
print(result)
