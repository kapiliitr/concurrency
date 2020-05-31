def tax(amount):
    brackets = [ [10000, 0.3],[20000, 0.2], [30000, 0.1], [None, .1]]

    total = 0
    accounted = 0
    for maxamount, ratio in brackets:
        if maxamount is None or amount <= maxamount:
            total += ratio*(amount - accounted)
            break
        else:
            total += ratio*(maxamount - accounted)
            accounted += maxamount
    return total

def main():
    t = int(input())
    while t > 0:
        amount = int(input())
        print(tax(amount))
        t -= 1


if __name__ == '__main__':
    main()