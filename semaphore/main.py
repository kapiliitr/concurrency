from threading import Thread, Lock, Condition
import random
import time

def waitrandom(m):
    r = random.Random()
    r.seed()
    time.sleep(r.randint(1,m))

class Semaphore:

    def __init__(self, N):
        self.n = N
        self.cv = Condition()

    def wait(self):
        with self.cv:
            self.cv.wait_for(lambda : self.n > 0)
            self.n -= 1

    def signal(self):
        with self.cv:
            self.n += 1
            self.cv.notify_all()

def enter(sem: 'Semaphore', i: str):
    sem.wait()
    print("Thread " + i + " entered.")
    waitrandom(5)
    print("Thread " + i + " exited.")
    sem.signal()

def main():
    m = 3
    t = 5
    sem = Semaphore(m)
    threads = []
    for i in range(1, t+1):
        threads.append(Thread(target=enter, args=(sem, str(i),)))
    for t in threads:
        t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':
    main()