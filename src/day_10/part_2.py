DEBUG = True

# ======= DISCLAIMER =======
# Works only for adpaters with distance of 1 or 3


def dbg_print(s):
    if DEBUG:
        print(s)


def solution(data):
    adapters = [int(x) for x in data.splitlines()]
    adapters.append(0)
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    group_of_elements_split_by_distance = {1: [], 2: []}
    # 0-1-2-4-5-7
    current_distance = 3
    dbg_print('Adpaters: {}'.format(adapters))
    for i in range(1, len(adapters)):
        delta_from_previous = adapters[i] - adapters[i - 1]
        dbg_print(f'Current number[{i}]: {adapters[i]}, delta from previous: {delta_from_previous}')
        if delta_from_previous < 3:
            if delta_from_previous != current_distance:
                group_of_elements_split_by_distance[delta_from_previous].append(1)
            group_of_elements_split_by_distance[delta_from_previous][-1] += 1
        current_distance = delta_from_previous
    dbg_print('groups_counter {}'.format(group_of_elements_split_by_distance))
    result = 1
    for counter in group_of_elements_split_by_distance[1]:
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
