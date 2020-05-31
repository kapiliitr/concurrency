import sys

def getK(arr, start, k, rev = False):
    begin = start
    end = start+k if not rev else start-k
    skip = 1 if not rev else -1
    for i in range(begin, end, skip):
        getI(arr, i)


def getI(arr, i):
    print(i)
    sys.stdout.flush()
    data = input()
    if data == 'N':
        sys.exit()
    arr[i-1] = int(data)


def complement(arr, b):
    for i in range(b):
        arr[i] = 1-arr[i]


def apply(arr, b, same, diff):
    action = [False, False, False, False] # Complement, Reverse, Complement & Reverse, No change

    if same is not None and diff is not None:
        sprev = arr[same-1]
        getI(arr, same)
        scur = arr[same-1]

        dprev = arr[diff-1]
        getI(arr, diff)
        dcur = arr[diff-1]


        if sprev == scur:
            if dprev == dcur:
                action[3] = True # No change
            else:
                action[1] = True # Reverse
        else:
            if dprev == dcur:
                action[2] = True # Complement and reverse
            else:
                action[0] = True # Complement

        # Reset since it gets applied at action below
        arr[same-1] = sprev
        arr[diff-1] = dprev
    elif same is not None:
        sprev = arr[same-1]
        getI(arr, same)
        getI(arr, same) # Dummy
        scur = arr[same-1]

        if sprev == scur:
            action[3] = True # No change
        else:
            action[0] = True # Complement

        arr[same-1] = sprev
    elif diff is not None:
        dprev = arr[diff-1]
        getI(arr, diff)
        getI(arr, diff) # Dummy
        dcur = arr[diff-1]

        if dprev == dcur:
            action[3] = True # No change
        else:
            action[0] = True # Complement

        arr[diff-1] = dprev

    if action[0]:
        # Complement
        complement(arr, b)
    elif action[1]:
        # Reverse
        arr.reverse()
    elif action[2]:
        # Complement and reverse
        complement(arr, b)
        arr.reverse()
    else:
        pass


def play(arr, b):
    if b <= 10:
        getK(arr, 1, b)
    else:
        # First 10 requests
        getK(arr, 1, 5)
        getK(arr, b, 5, True)

        same = None
        diff = None
        for i in range(1, 6):
            if arr[i-1] == arr[-i]:
                same = i
            else:
                diff = i

        # 11th & 12th requests
        apply(arr, b, same, diff)

        index = 6
        while index+4 <= b // 2:
            # Next 8 requests
            getK(arr, index, 4)
            getK(arr, b-index+1, 4, True)

            if same is None:
                for i in range(index, index+4):
                    if arr[i-1] == arr[-i]:
                        same = i
            if diff is None:
                for i in range(index, index+4):
                    if arr[i-1] != arr[-i]:
                        diff = i

            # Next 2 requests
            apply(arr, b, same, diff)

            index += 4

        # Next 2 requests
        getK(arr, b//2, 2)


def main():
    t, b = [int(s) for s in input().split(' ')]
    for i in range(1, t+1):
        arr = [0]*b
        play(arr, b)
        print(''.join(map(str, arr)))
        sys.stdout.flush()
        if input() == 'N':
            sys.exit()

if __name__ == '__main__':
    main()