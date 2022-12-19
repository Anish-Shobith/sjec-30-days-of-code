a=int(input())
b=int(input())
for i in range(a, b+1):
    if i % 3 == 0:
        print('Foo')
    elif i % 2 == 0 and i % 3 != 0:
        print('Bar')
    elif i % 2 == 1 and i % 3 != 0:
        print('Baz')