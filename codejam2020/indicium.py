import sys
import time

def getvalidvalues(mat, n, i, j):
    values = set([k for k in range(1,n+1)])

    for k in range(n):
        values.discard(mat[i][k])
        values.discard(mat[k][j])

    return list(values)

def settrace(mat, n, k):
    q = k // n
    r = k % n
    for i in range(n):
        mat[i][i] = q
        if r:
            mat[i][i] += 1
            r -= 1

def checktrace(mat, n, k):
    t = 0
    for i in range(n):
        t += mat[i][i]
    return t == k

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

def visit2(mat, n, k, i, j):
    vals = getvalidvalues(mat, n, i, j)
    if not vals:
        return False
    if i == n-1 and j == n-1:
        mat[i][j] = vals[0]
        if checktrace(mat, n, k):
            return True
        else:
            mat[i][j] = 0
            return False

    next_i, next_j = getnext(n, i, j)
    for v in vals:
        mat[i][j] = v
        if visit2(mat, n, k, next_i, next_j):
            return True
    mat[i][j] = 0
    return False

def indicium(n, k):
    mat = [[0 for i in range(n)] for j in range(n)]

    settrace(mat, n, k)
    if visit(mat, n, 0, 0):
        return mat

    if k % n != 0:
        mat = [[0 for i in range(n)] for j in range(n)]
        if visit2(mat, n, k, 0, 0):
            return mat

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