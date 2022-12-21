x=input
p=int
print('\n'.join([('Foo'if i%3==0 else'Bar'if i%2==0 else'Baz')for i in range(p(x()),p(x())+1)]))