from threading import *
import random
import time

def waitrandom(m):
    r = random.Random()
    r.seed()
    time.sleep(r.randint(1,m))

class UnisexBathroom:

    def __init__(self):
        self.men = Semaphore(3)
        self.women = Semaphore(3)
        self.menlock = Lock()
        self.womenlock = Lock()
        self.mencount = 0
        self.womencount = 0
        self.empty = Semaphore(1)

    def entermale(self, i):
        waitrandom(2)
        with self.men:
            with self.menlock:
                if self.mencount == 0:
                    print("Man " + i + " waiting for empty.")
                    self.empty.acquire()
                self.mencount += 1
            print("Man " + i + " entered.")
            with self.menlock:
                self.mencount -= 1
                print("Man " + i + " exited.")
                if self.mencount == 0:
                    self.empty.release()

    def enterfemale(self, i):
        waitrandom(2)
        with self.women:
            with self.womenlock:
                if self.womencount == 0:
                    print("Woman " + i + " waiting for empty.")
                    self.empty.acquire()
                self.womencount += 1
            print("Woman " + i + " entered.")
            with self.womenlock:
                self.womencount -= 1
                print("Woman " + i + " exited.")
                if self.womencount == 0:
                    self.empty.release()


def main():
    obj = UnisexBathroom()
    men = []
    female = []
    total = 20
    for i in range(total):
        men.append(Thread(target=obj.entermale, args=(str(i),)))
        female.append(Thread(target=obj.enterfemale, args=(str(i),)))
    for i in range(total):
        men[i].start()
        female[i].start()
    for i in range(total):
        men[i].join()
        female[i].join()


if __name__ == '__main__':
    main()