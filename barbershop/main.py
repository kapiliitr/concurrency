from threading import *
import time

closeShop = False

class Barbershop:

    def __init__(self, N):
        self.chairs = N
        self.remaining = N
        self.mutex = Semaphore(1)
        self.barberfree = Semaphore(1)
        self.customerwaiting = Semaphore(0)

    def getHairCut(self, index):
        with self.mutex:
            if self.remaining == 0:
                print("No available chairs, leaving " + index)
                return
            self.remaining -= 1
            print("Taken seat " + index)
        self.customerwaiting.release()
        self.barberfree.acquire()
        with self.mutex:
            print("Getting hair cut " + index)
            self.remaining += 1

    def cutHair(self):
        self.customerwaiting.acquire()
        time.sleep(2)
        self.barberfree.release()

def cut_hair(obj: 'Barbershop'):
    global closeShop
    while not closeShop:
        obj.cutHair()

def enter_shop(obj: 'Barbershop', index: int):
    time.sleep(index)
    obj.getHairCut(str(index))

def main():
    global closeShop
    obj = Barbershop(5)
    customers = []
    barber = Thread(target=cut_hair, args=(obj,))
    for i in range(50):
        customers.append(Thread(target=enter_shop, args=(obj, i,)))
    barber.start()
    for t in customers:
        t.start()
    for t in customers:
        t.join()
    closeShop = True
    obj.customerwaiting.release()
    barber.join()


if __name__ == '__main__':
    main()