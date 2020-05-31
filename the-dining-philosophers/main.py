import threading

class DiningPhilosophers:

    def __init__(self):
        self.forks = [threading.BoundedSemaphore() for i in range(5)]
        self.barrier = threading.Barrier(5)

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:

        leftfork = philosopher
        rightfork = (philosopher+1) % 5

        toeat = True

        def trypickforksandeat(leftfork ,rightfork):
            nonlocal toeat

            def pickforksandeat():
                pickLeftFork()
                pickRightFork()
                eat()
                putRightFork()
                putLeftFork()

            if self.forks[leftfork].acquire(blocking=False):
                if self.forks[rightfork].acquire(blocking=False):
                    pickforksandeat()
                    print("Philosopher " + str(philosopher) + " has eaten")
                    toeat = False
                    self.forks[rightfork].release()
                self.forks[leftfork].release()

        while toeat:
            if philosopher % 2 == 0:
                trypickforksandeat(leftfork, rightfork)
            else:
                trypickforksandeat(rightfork, leftfork)

        self.barrier.wait()

def thinkoreat(obj: 'DiningPhilosophers', id: int):
    obj.wantsToEat(id, lambda : None, lambda : None,lambda : None,lambda : None,lambda : None)

def main():
    obj = DiningPhilosophers()
    thread0 = threading.Thread(target=thinkoreat, args=(obj, 0,))
    thread1 = threading.Thread(target=thinkoreat, args=(obj, 1,))
    thread2 = threading.Thread(target=thinkoreat, args=(obj, 2,))
    thread3 = threading.Thread(target=thinkoreat, args=(obj, 3,))
    thread4 = threading.Thread(target=thinkoreat, args=(obj, 4,))
    thread0.start()
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread0.join()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

if __name__ == "__main__":
    main()