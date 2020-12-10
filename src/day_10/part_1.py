def solution(data):
    numbers = [int(x) for x in data.splitlines()]
    numbers.sort()
    counters = {1: 0, 2: 0, 3: 0}
    for i in range(len(numbers)):
        if i == 0:
            counters[numbers[i]] += 1
            continue
        counters[numbers[i] - numbers[i - 1]] += 1

    counters[3] += 1
    return counters[1] * counters[3]
