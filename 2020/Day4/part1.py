import re

r1 = r'byr: (cid: )?ecl: eyr: hcl: hgt: iyr: pid:'

def check_passport(passport):
    m = ' '.join(sorted(re.findall(r'[a-zA-Z]{3}:', passport)))
    if re.match(r1, m):
        return 1
    return 0


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = f.read()
    passports = []
    tmp_passport = []
    counter = 0
    for line in input.splitlines():
        if line != '':
            tmp_passport.append(line)
        else:
            counter += check_passport(' '.join(tmp_passport))
            tmp_passport = []
    print(counter)

#byr (Birth Year)
#iyr (Issue Year)
#eyr (Expiration Year)
#hgt (Height)
#hcl (Hair Color)
#ecl (Eye Color)
#pid (Passport ID)
#cid (Country ID) -> optional