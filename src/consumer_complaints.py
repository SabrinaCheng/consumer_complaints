#!/usr/bin/env python3

import time
import csv
import sys

def print_time_used(start_time):
    elapsed_time = time.time() - start_time
    print("Time used: %1.6fs" % elapsed_time)

def get_col_idx(header, selected_cols):
    """get column indices of selected columns"""
    selected_col_dict = {col:i for i, col in enumerate(header) if col in set(selected_cols)}
    return [selected_col_dict[col] for col in selected_cols]

def read_csv(input_filename, selected_cols = None):
    """read csv file and get selected columns as array of arrays"""
    start_time = time.time()
    with open(input_filename, 'r') as file:
        reader = csv.reader(file, delimiter=",")
        # get header
        header = next(reader)
        # get column indices of selected columns
        if selected_cols is None:
            selected_cols = header
        selected_idx = get_col_idx(header = header, selected_cols = selected_cols)
        #get selected data 
        data = [[row[i] for i in selected_idx]for row in reader]
    print("Data reading completed.", end="")
    print_time_used(start_time)
    return data

def get_year(data):
    """get first element as year from data splitted by "-" """ 
    return data.split("-")[0]

def main(input_filename, output_filename):
    # load data
    selected_cols = ["Product", "Date received", "Company"]
    data = read_csv(input_filename=input_filename, selected_cols=selected_cols)
    prod_col_idx, date_col_idx, comp_col_idx = list(range(3))
    
    # count frequency
    start_time = time.time()
    cnt_dict = {}
    for i, row in enumerate(data):
        try:
            product = row[prod_col_idx].lower()
            year = get_year(row[date_col_idx])
            company = row[comp_col_idx]

            id = product, year
            if id in cnt_dict:
                cnt_dict[id][company] = cnt_dict[id].get(company, 0) + 1
            else:
                cnt_dict[id] = {company: 1}

        except Exception as e:
            print("Counting error in row no. %d" % i)
            print(row)
            return

    # calculate variables
    output_list = []
    for id in sorted(cnt_dict):
        product, year = id
        id_cnt_dict = cnt_dict[id]
        # total number of complaints received for that product and year
        complaints_cnts_list = id_cnt_dict.values()
        total_complaints_cnt = sum(complaints_cnts_list)
        # total number of companies receiving at least one complaint for that product and year
        company_cnt = len(id_cnt_dict)
        # highest percentage (rounded to the nearest whole number) of total complaints filed 
        # against one company for that product and year
        max_percentage = round((max(complaints_cnts_list) / total_complaints_cnt) * 100)
        
        output_list.append(
            [product, year, str(total_complaints_cnt), str(company_cnt), str(max_percentage)])

    print("Data processing completed.", end="")
    print_time_used(start_time=start_time)

    # output to csv
    start_time = time.time()

    with open(output_filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(output_list)

    print("Output file writing completed.", end="")
    print_time_used(start_time=start_time)

if __name__ == "__main__":
    if(len(sys.argv) != 3):
        raise(Exception("Error: expected 2 arguments"))

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    start_time = time.time()

    # input_filename = "../input/complaints.csv"
    # output_filename = "../output/report.csv"
    main(input_filename, output_filename)

    print("=== Program completed ===", end="\n")
    print_time_used(start_time=start_time)


