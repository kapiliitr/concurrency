from threading import *

MAX_ITER = 10
i = 0
eating = True

class DiningSavages:

    def __init__(self, M):
        self.pot_size = M
        self.available = 0
        self.fullPot = Semaphore(0)
        self.emptyPot = Semaphore(0)
        self.mutex = Semaphore(1)

    def eat(self):
        with self.mutex:
            if self.available > 0:
                self.available -= 1
                print("Savage eating " + str(current_thread().ident))
            if self.available == 0:
                self.emptyPot.release()
                self.fullPot.acquire()

    def cook(self):
        self.emptyPot.acquire()
        print("Cook cooking " + str(current_thread().ident))
        self.available = self.pot_size
        self.fullPot.release()

def cook(obj: 'DiningSavages', lock: 'Lock'):
    global eating
    while True:
        with lock:
            if not eating:
                break
        obj.cook()

def savage(obj: 'DiningSavages', lock: 'Lock'):
    global i
    while i < MAX_ITER:
        with lock:
            i += 1
        obj.eat()

def main():
    global eating
    obj = DiningSavages(5)
    savages = []
    l = Lock()
    l2 = Lock()
    chef = Thread(target=cook, args=(obj,l2,))
    savages.append(Thread(target=savage, args=(obj,l,)))
    savages.append(Thread(target=savage, args=(obj,l,)))
    savages.append(Thread(target=savage, args=(obj,l,)))
    savages.append(Thread(target=savage, args=(obj,l,)))
    savages.append(Thread(target=savage, args=(obj,l,)))
    chef.start()
    for t in savages:
        t.start()
    for t in savages:
        t.join()
    with l2:
        eating = False
    obj.emptyPot.release()
    chef.join()


if __name__ == '__main__':
    main()