import sys
import time
import collections

def getvalidvalues(mat, n, i, j):
    values = set([k for k in range(1,n+1)])

    for k in range(n):
        values.discard(mat[i][k])
        values.discard(mat[k][j])

    return list(values)


def getnext(n, i, j):
    if j != n-1:
        return (i, j+1)
    if i != n-1:
        return (i+1, 0)
    return None

def visit(mat, n, i, j):
    if i == n-1 and j == n-1:
        return True
    next_i, next_j = getnext(n, i, j)
    if i == j:
        return visit(mat, n, next_i, next_j)
    vals = getvalidvalues(mat, n, i, j)
    if not vals:
        return False
    for v in vals:
        mat[i][j] = v
        if visit(mat, n, next_i, next_j):
            return True
    mat[i][j] = 0
    return False

def reset(mat, n):
    for i in range(n):
        for j in range(n):
            mat[i][j] = 0

def settrace(mat, n, arr):
    for i in range(n):
        mat[i][i] = arr[i]

def getarrfromway(way, n):
    arr = [0]*n
    i = 0
    for k, v in way.items():
        while v:
            arr[i] = k
            v -= 1
            i += 1
    return arr

def getsimpleway(n, k):
    arr = collections.Counter()
    q = k // n
    r = k % n
    for i in range(n):
        if r:
            arr[q+1] += 1
            r -= 1
        else:
            arr[q] += 1
    return arr


def getanotherway(way, n):
    s = list(filter(lambda x: x < n and way[x] > 0, way))
    if not s:
        return False
    q = max(s)
    t = list(filter(lambda x: (x == q and way[x] > 1) or (x < q and way[x] > 0), way))
    if not t:
        return False

    p = max(t)
    if q < n and p > 1:
        way[q+1] += 1
        way[q] -= 1
        way[p] -= 1
        way[p-1] += 1
        return True

    return False

def getways(n, k):
    ways = []
    way = getsimpleway(n, k)
    ways.append(getarrfromway(way, n))
    while getanotherway(way, n):
        ways.append(getarrfromway(way, n))
    return ways

def indicium(n, k):
    mat = [[0 for i in range(n)] for j in range(n)]

    for way in getways(n, k):
        settrace(mat, n, way)
        if visit(mat, n, 0, 0):
            return mat
        reset(mat, n)

    return None

def printmatrix(mat, n):
    for i in range(n):
        print(' '.join(map(str, mat[i])))
        sys.stdout.flush()

def main():
    t1 = time.time()
    t = int(input())
    for t in range(1, t+1):
        n, k = [int(s) for s in input().split(' ')]
        mat = indicium(n,k)
        if not mat:
            print('Case #', t, ': IMPOSSIBLE', sep='')
            sys.stdout.flush()
        else:
            print('Case #', t, ': POSSIBLE', sep='')
            sys.stdout.flush()
            printmatrix(mat, n)
    t2 = time.time()
    print('Total time = ',t2-t1)

if __name__ == '__main__':
    main()