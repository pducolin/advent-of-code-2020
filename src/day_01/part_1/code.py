def main():
  with open('input.txt') as f:
    total = 2020
    complementars = set()
    for input_line in f.read().split():
      value = int(input_line)
      if value in complementars:
        result = value * (total - value)
        print('🎉 Result is {}'.format(result))
        return
      complementars.add(total - value)

if __name__ == "__main__":
  main()