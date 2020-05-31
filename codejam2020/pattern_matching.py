import sys

def match(patterns, n):
    pass


def main():
    numcases = int(input())
    for t in range(numcases):
        m = int(input())
        patterns = []
        for i in range(m):
            patterns.append(input())
        k = match(patterns, m)
        print('Case #', t+1, ': ', k, sep='')

if __name__ == '__main__':
    main()