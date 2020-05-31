from threading import Thread, Lock, Condition
import random
import time

def waitrandom(m):
    r = random.Random()
    r.seed()
    time.sleep(r.randint(1,m))

class Barrier:

    def __init__(self, N):
        self.n = N
        self.cur = 0
        self.cv = Condition()
        self.state = 0 # 0 - entering, 1 - exiting

    def wait(self):
        with self.cv:
            self.cv.wait_for(lambda : self.state == 0)
            self.cur += 1
            if self.cur == self.n:
                self.state = 1
                self.cv.notify_all()
            else:
                self.cv.wait_for(lambda : self.state == 1)
            self.cur -= 1
            if self.cur == 0:
                self.state = 0
                self.cv.notify_all()

def enter(sem: 'Barrier', i: str):
    waitrandom(5)
    print("Thread " + i + " waiting to enter.")
    sem.wait()
    print("Thread " + i + " exited.")

def main():
    m = 3
    t = 6
    sem = Barrier(m)
    threads = []
    for i in range(1, t+1):
        threads.append(Thread(target=enter, args=(sem, str(i),)))
    for t in threads:
        t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':
    main()