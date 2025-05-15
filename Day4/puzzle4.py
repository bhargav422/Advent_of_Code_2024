
import sys
from collections import defaultdict
from itertools import groupby, product
if __name__ == '__main__':
    if len(sys.argv) > 2:
        print(f"Usage: {sys.argv[0]} <file.py>")
        sys.exit(1)

    file = sys.argv[1]
    with open(file, 'r') as f:
        ls = f.read().strip().split('\n')

    boards = defaultdict(str)
    boards |= {x + 1j * y: i for x, l in enumerate(ls)
                for y, i in enumerate(l)}
    octdir = {i + 1j*j for (i, j) in set(product((-1,0,1),(-1,0,1))) - {0, 0}}

    sum_of_pb = sum([boards[z + i * dz]for i in range(4)]==["X", "M", "A", "S"]
                    for z in list(boards.keys())
                    for dz in octdir)
    print(sum_of_pb)

    # part 2
    res = 0
    for z in list(boards.keys()):
        if boards[z] == "A":
            corners = [
                boards[z + 1 + 1j],
                boards[z + 1 - 1j],
                boards[z - 1 - 1j],
                boards[z - 1 + 1j]
            ]
            if (corners.count("M") == 2
                and corners.count("S") == 2
                and boards[z - 1 -1j] != boards[z + 1 + 1j]):
                res += 1
    print(res)