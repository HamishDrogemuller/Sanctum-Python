#IF and Else Statements
for n in range(1,101):
    if n % 15 == 0:
        print('fizzbuzz')
    else:
        if n % 3 == 0:
            print('fizz')
        else:
            if n % 5 == 0:
                print('buzz')
            else:
                print(n)

#ElIF Statements
for n in range(1,101):
    if n % 15 == 0:
        print('fizzbuzz')
    elif n % 3 == 0:
        print('fizz')
    elif n % 5 == 0:
        print('buzz')
    else:
        print(n)

#ternary
n = 101

fizzBuzz = 'Fizz' if n % 3 == 0 else 'Buzz' if n % 5 == 0 else 'FizzBuzz' if n % 15 == 0 else n


#Tuple FizzBuzz
def fizzBuzzTuples(n = int(input("Enter Fizz: ")),m = int(input("Enter Buzz: ")),o = int(input("Enter Length: "))):
    for i in range(1,o):
        if i % m == 0 and i % o == 0:
            print('FizzBuzz')
        elif i % m == 0:
            print('Fizz')
        elif i % o == 0:
            print('Buzz')
        else:
            print(i)


#Other
for n in range(int(input("Input first number: ")),int(input("Input last number: "))):
    if n % 15 == 0:
        print('fizzbuzz')
    else:
        if n % 3 == 0:
            print('fizz')
        else:
            if n % 5 == 0:
                print('buzz')
            else:
                print(n)


#While

