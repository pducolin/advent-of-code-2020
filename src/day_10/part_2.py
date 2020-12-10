def solution(data):
    numbers = [int(x) for x in data.splitlines()]
    numbers.append(0)
    numbers.sort()
    counters = {1: 0, 2: 0, 3: 0}
    groups_counters = []
    previous_delta = 0
    print('Numbers: {}'.format(numbers))
    for i in range(len(numbers) - 1):
        delta_from_next = numbers[i + 1] - numbers[i]
        counters[delta_from_next] += 1
        print('Current number[{}]: {}, delta from next: {}'.format(i, numbers[i], delta_from_next))
        if delta_from_next < 3:
            if previous_delta != delta_from_next:
                groups_counters.append(1)
            groups_counters[-1] += 1
        previous_delta = delta_from_next

    print('groups_counter {}'.format(groups_counters))
    counters[3] += 1
    result = 1
    for counter in groups_counters:
        if counter < 3:
            continue

        if counter == 3:
            result *= 2
            continue

        if counter == 4:
            result *= 4
            continue

        result *= (counter - 3) * 4 - 1

    return result
