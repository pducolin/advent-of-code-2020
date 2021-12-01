DEBUG = False

def dbg_print(s):
    if DEBUG:
        print(s)

def solution(data):
    counter = 0
    numbers = [int(line) for line in data.split()]
    sum_a = -1
    sum_b = -1
    for i in range(3,len(numbers)):
        sum_a = sum(numbers[i - 3:i])
        sum_b = sum(numbers[i-2:i+1])
        dbg_print(f'i: {i}, sum_a: {sum_a}, sum_b: {sum_b}')
        if sum_b > sum_a:
            counter += 1
      
    return counter
    
