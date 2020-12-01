def main():
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


if __name__ == "__main__":
  main()