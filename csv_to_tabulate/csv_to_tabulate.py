import sys
import csv
from tabulate import tabulate

def main():
    csv_to_tabulate()

def csv_to_tabulate():
    # confirm only one command argument was given
    one_arg()

    # confirm that its a csv file
    file_name = sys.argv[1].lower()

    if file_name.split(".")[-1] != "csv":
        print(sys.argv[1])
        sys.exit("Not a CSV file")
    # confirm that the file exists and read the file and store its contents in a var
    menue = []
    try:
        with open(file_name) as file:
            rows = csv.reader(file)
            for row in rows:
                menue.append(row)
    except FileNotFoundError:
        sys.exit("File not found")
    # print in a table format
    print(tabulate(menue, headers="firstrow", tablefmt="outline" ))

    
def one_arg():
    # confirm only one command argument was given
    if len(sys.argv) > 2:
        sys.exit("Too many command line arguments one argument expected")
    elif len(sys.argv) < 2:
        sys.exit("Too few command line arguments one argument expected")

if __name__ == "__main__":
    main()