import os
from collections import defaultdict
from datetime import datetime
import threading
import time
from multiprocessing import Process

"""
Python Playground
"""

hello = "hello world"
print(hello)

#Class Examples

#Dictionary
animals = {
    'a': 'aardvark',
    'b': 'baboon',
    'c': 'coati'
}

print(animals['a'])

animals['d'] = 'donkey'

animals2 = {
    'a': ['aardvark', 'antelope'],
    'b': ['baboon', 'boar'],
}
animals2['b'].append('buffalo')

animals2['c'] = ['coati', 'cobra']

if 'c' not in animals2:
    animals2['c'] = []

animals2['c'].append('camel')

animals3 = defaultdict(list)

#dict
animals3['e'].append('elephant')

#lists
myList = [1,2,3,4,5]
[2*item for item in myList]

myList2 = list(range(100))
filteredList = [item for item in myList2 if item % 2 == 0]

print(filteredList)

myString = 'my name is HCStrix. I live in NZ'
myString.split('.')

def cleanWord(word):
    return word.replace('.', '').lower()

[cleanWord(word) for word in myString.split()]

[[cleanWord(word) for word in sentence.split()] for sentence in myString.split('.')]

#dictList
animalList = [('aardvark', 'a'), ('baboon', 'b'), ('coati', 'c')]
animals = {item[0]: item[1] for item in animalList}
print('animals')

animals ={key: value for key, value in animalList}
print('animals')

print('animals.items()')

list(animals.items())

[{'letter': key, 'name': value} for key, value in animals.items()]

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

fizzBuzz = 'Fizz' if n % 3 ==0 else n

#While
wait_until = datetime.now().second + 2

while datetime.now().second != wait_until:
    pass

print(f'We are at {wait_until} seconds')

#OOP

class dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4

    def bark(self):
        print(f'{self.name} is barking')

myDog = dog('Fido')
print(myDog.name)
print(myDog.legs)

class cat:

    _legs = 4

    def __init__(self, name):
        self.name = name

    def getLegs(self):
        return self._legs

    def meow(self):
        print(f'{self.name} is meowing')

# Exception

class CustomException(Exception):
    pass    

def causeError():
    raise CustomException('You called causeError Function')

#Threading

def longSquare(num, results):
    time.sleep(1)
    results[num] = num**2

results = {}

t1 = threading.Thread(target=longSquare, args=(1,))
t2 = threading.Thread(target=longSquare, args=(2,))

t1.start()
t2.start()

t1.join()
t2.join()

print(results)


def longSquare(num, results):
    time.sleep(1)
    results[num] = num**2

results = {}
threads = [threading.Thread(target=longSquare, args=(n, results)) for n in range(0,10)]
[t.start() for t in threads]
[t.join() for t in threads]

print(results)


