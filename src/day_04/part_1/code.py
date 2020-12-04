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
    rows = [x for x in f.read().split('\n')] 
    passport = set()
    counter = 0
    for i in range(len(rows)):
      row = rows[i]
      for element in row.split(' '):
        passport.add(element.split(':')[0])
      if not row or i == len(rows) - 1:
        if is_valid_passport(passport):
          counter += 1
        passport.clear()
        continue
  print('🎉 Result is {}'.format(counter))

if __name__ == "__main__":
  solution()