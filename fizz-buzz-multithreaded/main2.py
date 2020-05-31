import threading

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.count = 1
        self.sem = threading.Semaphore()
        self.sem3 = threading.Semaphore(0)
        self.sem5 = threading.Semaphore(0)
        self.sem35 = threading.Semaphore(0)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while self.isvalid():
            self.sem3.acquire()
            if self.count <= self.n:
                printFizz()
            self.count += 1
            self.next()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while self.isvalid():
            self.sem5.acquire()
            if self.count <= self.n:
                printBuzz()
            self.count += 1
            self.next()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while self.isvalid():
            self.sem35.acquire()
            if self.count <= self.n:
                printFizzBuzz()
            self.count += 1
            self.next()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while self.isvalid():
            self.sem.acquire()
            if self.count <= self.n:
                printNumber(self.count)
            self.count += 1
            self.next()

    def next(self):
        if self.count%3 == 0 and self.count%5 == 0:
            self.sem35.release()
        elif self.count%3 == 0:
            self.sem3.release()
        elif self.count%5 == 0:
            self.sem5.release()
        else:
            self.sem.release()

    def isvalid(self):
        if self.count > self.n:
            self.sem.release()
            self.sem3.release()
            self.sem5.release()
            self.sem35.release()
            return False
        return True

def main():
    obj = FizzBuzz(15)
    thread1 = threading.Thread(target=lambda x: x.fizz(lambda: print("fizz")), args=(obj,))
    thread2 = threading.Thread(target=lambda x: x.buzz(lambda: print("buzz")), args=(obj,))
    thread3 = threading.Thread(target=lambda x: x.fizzbuzz(lambda: print("fizzbuzz")), args=(obj,))
    thread4 = threading.Thread(target=lambda x: x.number(lambda x: print(str(x))), args=(obj,))
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

if __name__ == '__main__':
    main()