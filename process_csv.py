'''A Permutation of size N is defined as a list containing all the integers 1 thru 
N in some order (not necessarily increasing order). Write a function which takes a 
CSV file and a permutation as input and rearranges the rows of a csv file according
 to the given permutation. Assume that the permutation is of the same size as the 
 number of rows in the CSV. E.g. say there are 4 rows in a csv file. A  permutation
 [2, 3, 1, 4], then the output CSV file will contain rows in the order: #2, #3, #1, 
 #4.'''

import csv

def arrangerows(input_file, output_file, permutation):
    with open(input_file) as ifile:
        reader = csv.reader(ifile)
        #header = next(reader)
        rows = [r for r in reader]

    with open(output_file, "w") as ofile:
        writer = csv.writer(ofile)
        #writer.writerow(header)
        for v in permutation:
            writer.writerow(rows[v])
            #print(rows[v])
    


arrangerows("paypal_report.csv", "rows_arranged.csv", [2,3,5,1,4])