import csv
import pandas as pd

# generate test data
output_list = []
with open("../../your-own-test_1/input/complaints.csv", "r") as file:
    csv_reader = csv.reader(file, delimiter=",")
    header = next(csv_reader)
    line_cnt = 0
    for row in csv_reader:
        if line_cnt > 10000:
            break
        # print(line_cnt)
        output_list.append(row)
        line_cnt += 1

    with open('complaints.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(i for i in header)
        writer.writerows(output_list)

# generate expected result
data = pd.read_csv('complaints.csv', usecols=["Product", "Date received", "Company"])
data["Date received"] = data["Date received"].str.split("-").str[0]
res = data.groupby(["Product", "Date received"]).agg(['count', 'nunique'])
print(res)
# df = pd.DataFrame(ou)
# selected_cols = ["Product", "Date received", "Company"]
# selected_idx = [i for i, n in enumerate(header) if n in selected_cols]

# # df = pd.DataFrame(np.vstack(output_list))
# print(selected_idx)
# print(df.head())