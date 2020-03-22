import csv
import random
import pandas as pd

# generate test data
def generate_test(output_filename):
    output_list = []
    with open("complaints.csv", "r") as file:
        csv_reader = csv.reader(file, delimiter=",")
        header = next(csv_reader)
        line_cnt = 0
        for row in csv_reader:
            if random.uniform(0, 1) <= 0.01:
                output_list.append(row)
                line_cnt += 1

    with open(output_filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(i for i in header)
        writer.writerows(output_list)
        
    print("Test data (n = %d) generated" % line_cnt)
    print(output_filename)


# generate expected result
def generate_expected_res(input_filename, output_filename):
    data = pd.read_csv(input_filename, usecols=["Product", "Date received", "Company"])
    data["Product"] = data["Product"].str.lower()
    data["Date received"] = data["Date received"].str.split("-").str[0]
    data["Company"] = data["Company"].str.lower()

    grouped = data.groupby(["Product", "Date received"])
    res = grouped.agg(['count', 'nunique'])
    total_complaints = res[('Company', 'count')]
    complaints_by_company = grouped.agg([lambda x: x.value_counts()[0]])
    res['max_percentage'] = round(complaints_by_company[('Company', '<lambda>')] / 
    total_complaints * 100).astype(int)

    res.to_csv(output_filename, header=False)
    print("Expected result completed")
    

if __name__ == "__main__":
    generated_test_data_filename = "tests/your-own-test_3/input/complaints.csv"
    generated_expected_res_filename = "tests/your-own-test_3/output/expected.csv"
    generate_test(generated_test_data_filename)
    generate_expected_res(generated_test_data_filename, generated_expected_res_filename)