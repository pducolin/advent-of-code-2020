def solution():
    counter = 0
    with open('input.txt') as f:
        lines = [x for x in f.read().split('\n')]
        for line in lines:
            rule, password = line.split(':')
            indexes, letter = rule.split()
            index_a, index_b = [int(x) for x in indexes.split('-')]
            letters_at_indexes = password[index_a] + password[index_b]
            if letters_at_indexes.count(letter) == 1:
                counter += 1
    print('🎉 Result is {}'.format(counter))


if __name__ == "__main__":
    solution()
