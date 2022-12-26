def isPrime(n):
  if n < 2:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True

m,n = map(int, input().split())

if m < 0 or n < 0:
    raise ValueError("m and n must be non-negative integers")
if m >= n:
    raise ValueError("m must be less than n")
  
primes = []
for i in range(m, n + 1):
    if isPrime(i):
      primes.append(i)
for i in range(len(primes) - 1):
    count = primes[i + 1] - primes[i] - 1
    print(f"{primes[i]} - {primes[i + 1]} : {count}")