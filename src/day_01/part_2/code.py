def solution_space_N():
  with open('input.txt') as f:
    total = 2020
    # O(N)
    numbers = [int(x) for x in f.read().split()]
    complementars = {}
    # O(N^2)
    for i in range(len(numbers)):
      a = numbers[i]
      if a in complementars:
        c = a
        a = complementars[c]['a']
        b = complementars[c]['b']
        print('🎉 Result is {}'.format(a*b*c))
        return
      for j in range(i, len(numbers)):
        b = numbers[j]
        complementars[total - a - b] = {'a': a, 'b': b }

def solution_space_const():
  with open('input.txt') as f:
    total = 2020
    # O(NlogN)
    sorted_numbers = sorted([int(x) for x in f.read().split()])
    # O(N^2)
    for i in range(len(sorted_numbers)):
      a = sorted_numbers[i]
      left_index = i + 1
      right_index = len(sorted_numbers) - 1
      while left_index < right_index:
        b = sorted_numbers[left_index]
        c = sorted_numbers[right_index]
        if a + b + c == total:
          print('🎉 Result is {}'.format(a*b*c))
          return

        if a + b + c < total:
          left_index += 1
          continue

        right_index -= 1


if __name__ == "__main__":
  solution_space_const()