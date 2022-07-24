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
n = 10

fizzBuzz = 'Fizz' if n % 3 == 0 else n
