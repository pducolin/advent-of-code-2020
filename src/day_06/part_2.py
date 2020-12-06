def solution():
  with open('input.txt') as f:
    groups = [x for x in f.read().split('\n\n')]
    counter = 0
    for group in groups:
      answers = []
      for answer in group.split('\n'):
        answers.append(set(list(answer)))
      counter += len(set.intersection(*answers))
    print('🎉 Result is {}'.format(counter))
    

if __name__ == "__main__":
  solution()
