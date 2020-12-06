import itertools

VALID_PASSPORT_FIELDS = set("""byr
iyr
eyr
hgt
hcl
ecl
pid""".split())

def is_valid_passport(passport):
  return len(VALID_PASSPORT_FIELDS - passport) == 0

def solution():
  with open('input.txt') as f:
    groups = [x for x in f.read().split('\n\n')] 
    passport = set()
    counter = 0
    for group in groups:
      passport.clear()
      for element in itertools.chain.from_iterable([x.split(' ') for x in group.split('\n')]):
        passport.add(element.split(':')[0])
      if is_valid_passport(passport):
          counter += 1
  print('🎉 Result is {}'.format(counter))

if __name__ == "__main__":
  solution()