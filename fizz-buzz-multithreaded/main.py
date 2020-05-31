import threading

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.count = 1
        self.cv = threading.Condition()
        self.fizzcond = lambda : self.count > self.n or self.count%3 ==0 and self.count%5!=0
        self.buzzcond = lambda : self.count > self.n or self.count%3 !=0 and self.count%5==0
        self.fizzbuzzcond = lambda : self.count > self.n or self.count%3 ==0 and self.count%5==0
        self.defaultcond = lambda : self.count > self.n or self.count%3 !=0 and self.count%5!=0

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while self.count <= self.n:
            with self.cv:
                self.cv.wait_for(self.fizzcond)
                if self.count <= self.n:
                    printFizz()
                self.count += 1
                self.cv.notify_all()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while self.count <= self.n:
            with self.cv:
                self.cv.wait_for(self.buzzcond)
                if self.count <= self.n:
                    printBuzz()
                self.count += 1
                self.cv.notify_all()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while self.count <= self.n:
            with self.cv:
                self.cv.wait_for(self.fizzbuzzcond)
                if self.count <= self.n:
                    printFizzBuzz()
                self.count += 1
                self.cv.notify_all()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while self.count <= self.n:
            with self.cv:
                self.cv.wait_for(self.defaultcond)
                if self.count <= self.n:
                    printNumber(self.count)
                self.count += 1
                self.cv.notify_all()

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