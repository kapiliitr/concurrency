def main():
    t = 0
    for i in range(2,6):
        for j in range(i, i*i + 1):
            print(i,j)
            t += 1
    print(t)


if __name__ == '__main__':
    main()