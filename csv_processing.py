
import csv

def del_col(inputf, outputf, col_num):
    """Delete given column from CSV file and 
    save remaining columns in a new CSV file

    Args:
    inputf (str): name of the input CSV file to be used
    outputf (str): name of the new CSV file to be created with
                   one column deleted
    col_num (int): column to be deleted from input file (zero-indexed)

    """
    with open (inputf) as ifile:
        reader = csv.reader(ifile)
        first_row = next(reader)
        num_cols = len(first_row)

        if col_num > num_cols:
            print("No such column exists")
            return

        with open(outputf, "w") as ofile:
            writer = csv.writer(ofile, quoting=csv.QUOTE_ALL)
            status = []
            for row in reader:
                if col_num == len(row):
                    status = row[:col_num-1]
                    writer.writerow(status)
                else:
                    status = row[:col_num-1] + row[col_num:]
                    writer.writerow(status)


def sortcol(input_file, out_file, col_num, sort_order = "asc"):
    """Sorts a column of a CSV file in given order, does not sort the entire row.

    Args:
    input_file (str): name of the input CSV file
    out_file (str): name of the output file to be saved
    col_num (int): column to be sorted
    sort_order (str): "asc" for Ascending or "desc" for Descending
    """
    with open(input_file) as ifile:
        reader = csv.reader(ifile)
        first_row = next(reader)
        colnums = len(first_row)
        
        if colnums > len(first_row):
            print("No such column exists")
            return

        sorted_col = []
        for row in reader:
            col = int(row[col_num-1])
            sorted_col.append(col)
        
        sorted_col = sorted(sorted_col)

        if sort_order == "desc":
            sorted_col.reverse()
            
        with open(out_file, "w") as ofile:
            writer = csv.writer(ofile)        
            for v in sorted_col:
                writer.writerow([v])


def full_sort(input_file, out_file, col_num):
    """Sort rows of a CSV file using given column with expanded selection.

    Args:
        input_file (str): name of CSV file to be sorted
        out_file (str): name of the sorted CSV file to be written into
        col_num (int): column to be used to sort the input CSV file (zero-indexed)

    """
    with open(input_file, 'r') as ifile:
        reader = csv.reader(ifile)
        first_row = next(reader)
        colnums = len(first_row)

        if colnums > len(first_row):
            print("No such column exists")
            return

        original_col_list = []
        for row in reader:
            col = int(row[col_num-1])
            original_col_list.append(col)
        
        sorted_col = sorted(original_col_list)    
        length = len(original_col_list)
        index_list = []
        rows = [r for r in reader]

        for i in range(length):
            for j in range(length):
                if sorted_col[i] == original_col_list[j]:
                    index_list.append(j)

        with open(out_file, "w") as ofile:
            writer = csv.writer(ofile)        
            for v in index_list:
                writer.writerow(rows[v])
