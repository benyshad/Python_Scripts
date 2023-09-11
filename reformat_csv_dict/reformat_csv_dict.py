import sys
import csv

def main():
    scourgify()

def scourgify():
    # # check for 2 args
    if arg_checker(3) == False:
        sys.exit("Please provide 2 arguments input.csv output.csv")

    output = []
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # open and read input file
    try:
        with open(input_file, "r") as input_file:
            rows = csv.DictReader(input_file)
            for row in rows:

                # swap first and last name
                row = swap(row)

                # create dict from csv
                output.append(row)

    except FileNotFoundError:
        sys.exit("File not found")

    #open and write to ouput file

    try:
        with open(output_file, "a") as output_file:
            writer = csv.DictWriter(output_file, fieldnames=["name", "house"])
            for row in output:
                writer.writerow(row)
    except FileNotFoundError:
        sys.exit("File not found")

def swap(row):
    first_name = row["name"].split(",")[-1]
    last_name = row["name"].split(",")[0]
    row["name"] = (first_name + ", " + last_name)
    return row

# check that proper amounts of args are given
def arg_checker(n):
    if len(sys.argv) == n:
        return True
    else:
        return False

if __name__ == "__main__":
    main()