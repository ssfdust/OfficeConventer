from threading import Thread
from time import sleep

class FullConverter(object):
    def __init__(self):
        self.state = 0
        self.prgbar_max = 0
        self.prgbar_val = 0

    def test(self):
        self.state = 1
        states = [1, 2, 3, 4]
        max_vals = [20, 15, 400, 900]
        for s, m in zip(states, max_vals):
            self.prgbar_max = 20
            self.run(self.prgbar_max)
            sleep(3)

    def run(self, max_val):
        self.prgbar_val = 0
        for i in range(max_val):
            self.prgbar_val += 1
            sleep(0.01)

    def run_thread(self):
        t = Thread(target=self.test)
        t.start()
