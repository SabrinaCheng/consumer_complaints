# Consumer Complaints

## Table of Contents
1. [Introduction](README.md#introduction)
1. [How to use](README.md#how-to-use)
1. [Design](README.md#design)
1. [Tests](README.md#test)


## Introduction
Consumer Financial Protection Bureau provides a database containing a collection of complaints about consumer financial products and services. This project identifies the number of complaints filed and how they're spread across different companies. The input file has the following columns: Date received, Product, Sub-product, Issue, Sub-issue, Consumer complaint narrative, Company public response, Company, State, ZIP code, Tags, Consumer consent provided?, Submitted via, Date sent to company, Company response to consumer, Timely response?, Consumer disputed?, Complaint ID. The output result contains information about financial product, year, the total number of complaints, number of companies receiving a complaint, and the highest percentage of complaints directed at a single company.


## How to use
This is a python3.7 program.
Run `sh run.sh`


## Design
1. Read input CSV file<br>
Python standard package "CSV" is used to read the input CSV file. Even though reading without using package also works(counting number of quotes and commas to split columns), according to my experiments, the running time is longer, which might be problematic when dealing with large datasets. To save memory, only three selected columns, Product, Date received, and Company, are read.

2. Clean data<br>
Product and Company names are converted to lowercase. Year information is extracted from Date received by getting the first element after splitting the string by "-".

3. Count number of complaints and companies, and then calculate the highest percentage of complaints directed at a single company<br>
Python dictionary is used to store counting data, with tuple consisting of product and year as key and another dictionary as value. The dictionaries in the dictionary have company name as key and count as value. For example, {(product, year): (company: 1}. To calculate target variables for a product and a specific year:
* total number of complaints received for that product and year<br>
 Sum up corresponding dictionary values.
 * total number of companies receiving at least one complaint for that product and year<br>
 Get the length of the corresponding dictionary.
 * highest percentage (rounded to the nearest whole number) of total complaints filed against one company for that product and year<br>
 Get the maximum number of complaints from the corresponding dictionary, divide it by the total number of complaints received for that product and year, and then round it to a whole number.

4. Output a csv file "report.csv"<br>
Python standard package "CSV" is used to write the results to a CSV file.

## Tests
The program passes test_1.
Another three test datasets(sample size is about 10000 to 15000 lines) are generated by randomly select data from the modest-sized dataset given by the challenge. Uniform random number selection from 0 to 1 is used. If the random number is smaller than or equals to 0.01, then that line of data is included in the test dataset; otherwise, that line of data is skipped. The program passes all of these three tests.   

