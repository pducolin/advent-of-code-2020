def solution(data):
    counter = 0
    numbers = [int(line) for line in data.split()]
    previous = numbers[0]
    for i in range(1,len(numbers)):
      if numbers[i] > previous:
        counter += 1
      previous = numbers[i]
    return counter
    
