def find(m, n):
    a = [0]*m
    for i in range(n-1, m):
        a[i] = sum(a[i-n:i]) or 1
    return a[m-1]
print(find(*map(int, input().split())))