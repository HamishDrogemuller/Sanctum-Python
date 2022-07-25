up_to = int(input("Enter Destination:"))

def fizz_buzz(up_to):
    fizz = 3
    buzz = 5


def fizz_buzz_tuple(up_to,):
        tuple1 = ()
        tuple2 = ()
        for n in range(up_to,):
            if n % 15 == 0:
                tuple2 = tuple1 + (n,"fizzbuzz")
                print(tuple1)
            elif n % 3 == 0:
                tuple2 = tuple1 + (n,"fizz")
                print(tuple1)
            elif n % 5 == 0:
                tuple2 = tuple1 + (n,"buzz")
                print(tuple1)
        else:
            tuple2 = tuple1 + (n,n)
            print(tuple2)

print(fizz_buzz_tuple(up_to))
print(type(fizz_buzz_tuple(up_to)))

def whileBuzz(n = int(input("Enter Fizz: ")), m = int(input("Enter Buzz: "))):
    while n < 100:
        if n % 3 == 0:
            print("buzz")
        elif n % 5 == 0:
            print("fizz")
        else:
            print(n)
        n = n + 1

print(whileBuzz())
