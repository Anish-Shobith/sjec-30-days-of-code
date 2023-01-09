def f(a, b):
  def c(n):
    s = 0
    while n != 1:
      n = n // 2 if n % 2 == 0 else 3 * n + 1
      s += 1
    return s

  return max(range(a, b+1), key=c)

print(f(*map(int, input().split())))