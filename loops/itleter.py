ls = [1,2,3,4,5]

it = iter(ls)

print(it.__next__())
print(next(it))
print(it.__next__())
print(it.__next__())


class test:
    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.num = self.num + 1
        return self.num 

num = test()

print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))


def topten():

    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
values = topten()

print(next(values))