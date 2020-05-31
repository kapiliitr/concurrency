import sys

def trace(mat, m):
    k = 0
    for i in range(m):
        k += mat[i][i]
    return k

def duprows(mat, m):
    r = 0
    for i in range(m):
        seen = set()
        for j in range(m):
            if mat[i][j] in seen:
                r += 1
                break
            else:
                seen.add(mat[i][j])
    return r

def dupcols(mat, m):
    c = 0
    for j in range(m):
        seen = set()
        for i in range(m):
            if mat[i][j] in seen:
                c += 1
                break
            else:
                seen.add(mat[i][j])
    return c

def vestigium(mat, m):
    k = trace(mat, m)
    r = duprows(mat, m)
    c = dupcols(mat, m)
    return (k, r, c)

def main():
    numcases = int(sys.stdin.readline())
    for t in range(numcases):
        m = int(sys.stdin.readline())
        mat = [[None for i in range(m)] for j in range(m)]
        for i in range(m):
            line = sys.stdin.readline().split()
            for j in range(m):
                mat[i][j] = int(line[j])
        k, r, c = vestigium(mat, m)
        print('Case #', t+1, ': ', k, ' ', r, ' ', c, sep='')

if __name__ == '__main__':
    main()