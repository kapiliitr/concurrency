import sys
import collections

class KeyValueStore:

    def __init__(self):
        self.keyValMap = {}
        self.valCountMap = collections.Counter()

    def set(self, name, value):
        if name in self.keyValMap:
            if self.keyValMap[name] != value:
                self.valCountMap[self.keyValMap[name]] -= 1
            else:
                return
        self.keyValMap[name] = value
        self.valCountMap[value] += 1

    def get(self, name):
        if name in self.keyValMap:
            return self.keyValMap[name]
        else:
            return "NULL"

    def unset(self, name):
        if name in self.keyValMap:
            self.valCountMap[self.keyValMap[name]] -= 1
            del self.keyValMap[name]

    def numWithValue(self, value):
        return self.valCountMap[value]

    def begin(self):
        pass

    def rollback(self):
        pass

    def commit(self):
        pass

def main():
    store = KeyValueStore()
    for line in sys.stdin:
        line = line.rstrip()
        command = line.split(" ")

        if command[0] == "SET":
            store.set(command[1], command[2])
        elif command[0] == "GET":
            print(store.get(command[1]))
        elif command[0] == "UNSET":
            store.unset(command[1])
        elif command[0] == "NUMWITHVALUE":
            print(store.numWithValue(command[1]))
        elif command[0] == "BEGIN":
            store.begin()
        elif command[0] == "ROLLBACK":
            store.rollback()
        elif command[0] == "COMMIT":
            store.commit()
        elif command[0] == "END":
            break

if __name__ == "__main__":
    main()