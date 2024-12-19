import numpy as np
import copy
UNSAFE_REPORT_LIST = []

def parse_list(file):
    """
    Parse every row in file
    """
    with open(file) as f:
        reader = f.readlines()
        list_of_reports = [(level_list.strip()) for level_list in reader ]

    int_list = []
    for report in list_of_reports:
        report = report.split(' ')
        report = [int(i) for i in report]
        int_list.append(report)

    return int_list

def check_reports(report):
    """
    Check a report whether if its safe or unsafe

    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.
    In the example above, the reports can be found safe or unsafe by checking those rules:

    7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
    1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
    9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
    1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
    8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
    1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

    :returns: 0 if report is Safe\n
              1 if report is Unsafe
    """

    report =  [report[i + 1] - report[i] for i in range(len(report) - 1)] 
    if (all(x < 0 and x in range(-3, 0) for x in report) or\
     all(x > 0  and x in range(1, 4) for x in report)):
        return True
    else:
        return False



if __name__ == '__main__':
    total = 0
    report_list = parse_list('input_data.txt')
    for reports in report_list:
        if check_reports(reports):
            total+=1
        else:
            for i in range(len(reports)):
                int_list = reports.copy()
                int_list.pop(i)
                if check_reports(int_list):
                    total += 1
                    break
    print(total)
