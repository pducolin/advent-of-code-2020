def solution():
    counter = 0
    with open('input.txt') as f:
        lines = [x for x in f.read().split('\n')]
        for line in lines:
            rule, password = line.split(':')
            min_max, letter = rule.split()
            rule_min, rule_max = [int(x) for x in min_max.split('-')]
            letter_in_password_count = password.count(letter)
            if letter_in_password_count >= rule_min and letter_in_password_count <= rule_max:
                counter += 1
    print('🎉 Result is {}'.format(counter))


if __name__ == "__main__":
    solution()
