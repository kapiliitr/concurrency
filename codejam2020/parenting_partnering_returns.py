import sys


def parent(chance):
    return 'C' if chance == 0 else 'J'


def assign(activities):
    cstack = []
    jstack = []
    for a in activities:
        while cstack and cstack[-1][1] <= a[0]:
            cstack.pop()
        while jstack and jstack[-1][1] <= a[0]:
            jstack.pop()
        if len(cstack) + len(jstack) >= 2:
            return False
        assignment = 0
        if cstack and not jstack:
            assignment = 1
        a[3][0] = assignment
        if not assignment:
            cstack.append(a)
        else:
            jstack.append(a)
    return True


def schedule(activities):
    activities.sort(key = lambda x: x[1], reverse=True)
    activities.sort(key = lambda x: x[0])
    n = len(activities)
    if not assign(activities):
        return 'IMPOSSIBLE'
    ret = [None for i in range(n)]
    for i in range(n):
        ret[activities[i][2]] = parent(activities[i][3][0])
    return ''.join(ret)


def main():
    numcases = int(sys.stdin.readline())
    for t in range(numcases):
        numactivites = int(sys.stdin.readline())
        activities = []
        for i in range(numactivites):
            line = sys.stdin.readline().split()
            start = int(line[0])
            end = int(line[1])
            activities.append((start, end, i, [None]))
        print('Case #', t+1, ': ', schedule(activities), sep='')

if __name__ == '__main__':
    main()