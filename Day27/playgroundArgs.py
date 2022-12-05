def add(*args):
    count=0
    print(type(args))
    for i in args:
        count+=i

    print(count)

add(2,3,4,5,1)