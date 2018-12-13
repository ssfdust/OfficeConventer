from time import sleep
from threading import Thread

class FullConverter(object):
    def __init__(self, data):
        self.state = 0
        self.errcode = 0
        self.outfile = None
        self.prgbar_max = 0
        self.prgbar_val = 0

    def test(self):
        states = [1, 2, 3, 4]
        max_vals = [20, 15, 400, 900]
        for s, m in zip(states, max_vals):
            if self.errcode:
                break
            self.state = s
            self.prgbar_max = m
            self.process(self.prgbar_max)
        self.outfile = '/tmp/demo.py'

    def process(self, max_val):
        self.prgbar_val = 0
        for i in range(max_val):
            self.prgbar_val += 1
            sleep(0.01)
            print('ok')

    def run(self):
        self.p = Thread(target=self.test)
        self.p.start()
