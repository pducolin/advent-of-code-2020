from src.common import load_input


def solution(data):
    groups = [x for x in data.split('\n\n')]
    counter = 0
    for group in groups:
        answers = []
        for answer in group.split('\n'):
            answers.append(set(list(answer)))
        counter += len(set.intersection(*answers))
    return counter


if __name__ == "__main__":
    print('🎉 Result is {}'.format(solution(load_input('input.txt'))))
