from threading import *
from collections import deque
import random
import time

def waitrandom():
    r = random.Random()
    r.seed()
    time.sleep(r.randint(0,2))

class LinkedList:

    def __init__(self):
        self.searches = 0
        self.inserts = 0
        self.deletes = 0
        self.mutex = Semaphore(1)
        self.queue = deque([])

    def search(self, i):
        waitrandom()
        sem = Semaphore(0)
        with self.mutex:
            self.searches += 1
            if self.deletes > 0:
                self.queue.append(sem)
            else:
                sem.release()
        sem.acquire()
        # Perform search
        print("Search by " + str(i))
        with self.mutex:
            self.searches -= 1
            if self.queue:
                next = self.queue.popleft()
                next.release()

    def insert(self, i):
        waitrandom()
        sem = Semaphore(0)
        with self.mutex:
            self.inserts += 1
            if self.deletes > 0 or self.inserts > 1:
                self.queue.append(sem)
            else:
                sem.release()
        sem.acquire()
        # Perform insert
        print("Insert by " + str(i))
        with self.mutex:
            self.inserts -= 1
            if self.queue:
                next = self.queue.popleft()
                next.release()

    def delete(self, i):
        waitrandom()
        sem = Semaphore(0)
        with self.mutex:
            self.deletes += 1
            if self.searches > 0 or self.inserts > 0 or self.deletes > 1:
                self.queue.append(sem)
            else:
                sem.release()
        sem.acquire()
        # Perform delete
        print("Delete by " + str(i))
        with self.mutex:
            self.deletes -= 1
            if self.queue:
                next = self.queue.popleft()
                next.release()

def main():
    obj = LinkedList()
    searchers = []
    inserters = []
    deleters = []
    total = 5
    for i in range(total):
        searchers.append(Thread(target=obj.search, args=(i,)))
        inserters.append(Thread(target=obj.insert, args=(i,)))
        deleters.append(Thread(target=obj.delete, args=(i,)))
    for i in range(total):
        searchers[i].start()
        inserters[i].start()
        deleters[i].start()
    for i in range(total):
        searchers[i].join()
        inserters[i].join()
        deleters[i].join()


if __name__ == '__main__':
    main()