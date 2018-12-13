from threading import Thread
from time import sleep

class A(object):
    def __init__(self):
        self.a = 1

    def s(self):
        while True:
            self.a = 4
            sleep(1)

    def c(self):
        t = Thread(target=self.s)
        t.start()
        sleep(5)
        print(self.a)


t = A()
t.c()
