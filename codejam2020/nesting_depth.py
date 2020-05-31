import sys

def depth(s):
    r = ''
    open = 0
    for c in s:
        n = int(c)
        while open < n:
            r += '('
            open += 1
        while open > n:
            r += ')'
            open -= 1
        r += c
    while open > 0:
        r += ')'
        open -= 1
    return r

def main():
    numcases = int(sys.stdin.readline())
    for t in range(numcases):
        print('Case #', t+1, ': ', depth(sys.stdin.readline().rstrip('\n')), sep='')

if __name__ == '__main__':
    main()