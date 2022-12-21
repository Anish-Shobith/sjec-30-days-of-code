x=int
i=input
def f(t):
  for i,x in enumerate(t):
    print(sorted(x)[i%3])
f([list(map(x,i().split()))for _ in range(x(i()))])