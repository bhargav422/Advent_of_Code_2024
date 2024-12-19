import numpy as np
import collections

def parse_list(file):
    x = []
    y = []
    with open(file) as f:
        reader = f.readlines()
        for lines in reader:
            line = lines.split('   ')
            x.append(line[0])
            y.append(line[1])
        
    return x, y

def find_total_path(l1, l2):
    """
    Find the total distance between eac list element

    :returns: sum of the total path
    """
    l1 = sorted(l1)
    l2 = sorted(l2)
    total = []
    sum_path = 0

    for a, b in list(zip(l1,l2)):
        total.append(np.abs(int(a)-int(b)))
        sum_path = sum(total)

    return sum_path

def find_similarity(l1, l2):
    """
    Find the similar count in second list if not present mark as 0

    :return: sum of a list with similar elements multiplied and non similar element as 0
    """
    similar_count = 0
    l1 = [int(x) for x in l1]
    l2 = [int(x) for x in l2]
    count_list = 0
    county = []
    count = collections.Counter(l2)

    for i in range(len(l1)):
        if l1[i] in count.keys():
            count_list = l1[i] * count[l1[i]]
            county.append(count_list)
        else:
            count_list = 0
            county.append(count_list)

    return sum(county)

if __name__ == '__main__':
    l1,l2 = parse_list("input_data.txt")
    sum_path = find_total_path(l1, l2)
    count_list = find_similarity(l1, l2)
