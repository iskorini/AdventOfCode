import re

four_digits = re.compile('^[0-9]{4}$')
hgt_cm = re.compile('^[0-9]{3}cm$')
hgt_in = re.compile('^[0-9]{2}in$')
hcl = re.compile('^#[a-zA-Z0-9_]{6}$')
ecl = re.compile('^(amb|blu|brn|gry|grn|hzl|oth)$')
pid = re.compile('^[0-9]{9}$')

validating_function = {
    'byr': lambda x: check_number(x, 1920, 2002),
    'iyr': lambda x: check_number(x, 2010, 2020),
    'eyr': lambda x: check_number(x, 2020, 2030),
    'hgt': lambda x: check_hgt(x),
    'hcl': lambda x: check_regex(x, hcl), 
    'ecl': lambda x: check_regex(x, ecl), 
    'pid': lambda x: check_regex(x, pid),
    'cid': lambda x: 0
}

def check_regex(value, regex):
    if regex.match(value):
        return 1
    return 0

def check_number(value, min, max, digits=4):
    if check_regex(value, four_digits) == 1:
        return int(int(value)>=min and int(value)<=max)
    return 0
 
def check_hgt(value):
    if check_regex(value, hgt_cm) == 1:
        return int(int(value[0:3]) >= 150 and  int(value[0:3]) <= 193)
    elif check_regex(value, hgt_in) == 1:
        return int(int(value[0:2]) >= 59 and int(value[0:2]) <= 76)
    return 0

def check_passport(value):
    tmp = 0
    for element in value.split(' '):
        tmp += validating_function[element[0:3]](element[4:])
    return int(tmp == 7)

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