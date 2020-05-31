all_sequences_set = set()

def next_sequences(pushed, index, cur_popped, cur_pushed):
    if index == len(pushed):
        if cur_pushed:
            return next_sequences(pushed, index, cur_popped+[cur_pushed[-1]], cur_pushed[:len(cur_pushed)-1])
        else:
            if tuple(cur_popped) not in all_sequences_set:
                all_sequences_set.add(tuple(cur_popped))
                return [cur_popped]
            else:
                return []
    else:
        cur_pushed.append(pushed[index])
        sequences = []
        for i in range(len(cur_pushed)+1):
            next_pushed = cur_pushed[:len(cur_pushed)-i]
            next_popped = cur_popped + cur_pushed[::-1][:i]
            for seq in next_sequences(pushed, index+1, next_popped, next_pushed):
                sequences.append(seq)
        return sequences

def all_sequences(pushed):
    return next_sequences(pushed, 0, [], [])

def main():
    pushed = [int(i) for i in input().split(',')]
    print(all_sequences(pushed))

if __name__ == '__main__':
    main()