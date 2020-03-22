import csv
import sys

# test
def test(actual, expected, report_filename):
    with open(actual, 'r') as t1, open(expected, 'r') as t2:
        fileone = t1.readlines()
        filetwo = t2.readlines()
    is_error = False
    for i, line in enumerate(filetwo):
        if line not in fileone:
            print("Error found at row no. %d!" % i)
            print(line)
            if not is_error:
                is_error = True
    print("Test completed")
    if not is_error:
        print("Test passed!")

if __name__ == "__main__":
    # test_1, your-own-test_1
    path = 'tests/your-own-test_3/'
    actual = path + 'output/report.csv'
    expected = path + 'output/expected.csv'
    report_filename = path + 'output/test_result.csv'
    test(actual, expected, report_filename)