import threading


def Hi():
    i = 1
    while (i<1000):
        print('Hi')
        i = i + 1

t1 = threading.Thread(target=Hi)
t2 = threading.Thread(target=Hi)

t1.start()
t2.start()

t1.join()
t2.join()

