from src.common import load_input


def solution(data):
    groups = [x for x in data.split('\n\n')]
    counter = 0
    for group in groups:
        answers = set()
        for answer in ''.join(group.split('\n')):
            answers.add(answer)
        counter += len(answers)
    return counter


if __name__ == "__main__":
    print('🎉 Result is {}'.format(solution(load_input('input.txt'))))
