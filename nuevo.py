def lamba(r, g):
    yield 231
y = lamba(3,4)



def g(x):
    yield from range(x, 0, -1)
    yield from range(x)
print(list(g(10)))