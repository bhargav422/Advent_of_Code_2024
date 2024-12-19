import re
def uncorrupted_mul(file):
    find = '^mul\(\d{1,3},\d{1,3}\)$'
    mul_pattern = re.compile(find)
    print(mul_pattern)
    count = 0
    with open(file) as fr:
        reader = fr.read()
    print(mul_pattern.match(reader))


    
if __name__ == '__main__':
    uncorrupted_mul('demo_data.txt')