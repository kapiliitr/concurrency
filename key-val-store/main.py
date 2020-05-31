import sys
import collections

class KeyValueStore:

    def __init__(self):
        # In memory representation of committed key-value pairs in a dictionary
        self.keyValMap = {}
        # In memory representation of committed value-count pairs in a dictionary
        self.valCountMap = collections.Counter()
        # List of ongoing transactions
        # Contains a tuple of the form (keyValMap, valCountMap)
        # Contains only the modifications done as part of the transaction
        self.transactions = []
        # Indicates the state of the transaction
        # Can be None - no txn running, Start - at least 1 txn running, Finish - all txns committed
        # State transitions-
        # None -> Start
        # Start -> Finish, None (on rollback everything)
        # Finish -> None
        self.transactionState = "None"

    def set(self, name, value):
        localKeyValMap = self.keyValMap
        localValCountMap = self.valCountMap
        # Set the key-value pair for the latest transaction
        if self.transactionState == "Start":
            localKeyValMap = self.transactions[-1][0]
            localValCountMap = self.transactions[-1][1]
        curVal = self.get(name)
        if curVal != "NULL":
            # Decrement the value count for the previous value of the key
            localValCountMap[curVal] -= 1
        localKeyValMap[name] = value
        localValCountMap[value] += 1

    def get(self, name):
        if self.transactionState == "Start":
            # Search for the value of the key in transaction modifications in reverse order
            for index in range(len(self.transactions) - 1, -1, -1):
                localKeyValMap = self.transactions[index][0]
                if name in localKeyValMap:
                    return localKeyValMap[name]
        # Search for the value of the key in committed state
        if name in self.keyValMap:
            return self.keyValMap[name]
        return "NULL"

    def unset(self, name):
        if self.transactionState != "Start":
            if name in self.keyValMap:
                self.valCountMap[self.keyValMap[name]] -= 1
            del self.keyValMap[name]
            return
        else:
            localKeyValMap = self.transactions[-1][0]
            localValCountMap = self.transactions[-1][1]
            localValCountMap[self.get(name)] -= 1
            localKeyValMap[name] = "NULL"

    def numWithValue(self, value):
        if self.transactionState != "Start":
            return self.valCountMap[value]
        else:
            count = self.valCountMap[value]
            for index in range(len(self.transactions)):
                localValCountMap = self.transactions[index][1]
                if value in localValCountMap:
                    count += localValCountMap[value]
            return count

    def begin(self):
        self.transactions.append(({}, collections.Counter()))
        self.transactionState = "Start"

    def rollback(self):
        if self.transactionState == "None":
            print("NO TRANSACTION")
            return
        self.transactions.pop()
        if len(self.transactions) == 0:
            self.transactionState = "None"

    def commit(self):
        if self.transactionState == "None":
            print("NO TRANSACTION")
            return
        self.transactionState = "Finish"
        for txn in self.transactions:
            for name, value in txn[0].items():
                if value == "NULL":
                    self.unset(name)
                else:
                    self.set(name, value)
        self.transactionState = "None"

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