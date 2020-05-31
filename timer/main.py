from threading import Thread, Lock, Condition
import random
import time

r = random.Random()
r.seed()

def getrandom(m):
    return r.randint(1,m)

class Timer:

    def __init__(self, interval, func):
        self.interval = interval
        self.func = func
        self.cv = Condition()
        self.state = 0 # 0 - not fired, 1 - fired, 2 - cancelled
        self.t = None

    def inner(self):
        time.sleep(self.interval)
        with self.cv:
            if self.state == 0:
                self.state = 1
                self.cv.notify()

    def start(self):
        with self.cv:
            self.t = Thread(target=self.inner)
            self.t.start()
            self.cv.wait_for(lambda : self.state != 0)
            if self.state != 2:
                self.t.join()
                self.func()

    def cancel(self):
        with self.cv:
            if self.state == 0:
                self.state = 2
                self.cv.notify()
                return True
        return False

def enter(i: int):
    timer = Timer(getrandom(3), lambda : print("Thread " + str(i) + " entered."))
    t = Thread(target=timer.start)
    t.start()
    time.sleep(getrandom(5))
    if timer.cancel():
        print("Thread " + str(i) + " cancelled.")
    t.join()

def main():
    t = 6
    threads = []
    for i in range(1, t+1):
        threads.append(Thread(target=enter, args=(i,)))
    for t in threads:
        t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':
    main()