def solution():
  with open('input.txt') as f:
    groups = [x for x in f.read().split('\n\n')]
    counter = 0
    for group in groups:
      answers = set()
      for answer in ''.join(group.split('\n')):
        answers.add(answer)
      counter += len(answers)
    print('🎉 Result is {}'.format(counter))
    

if __name__ == "__main__":
  solution()
