import sys

def main():
    lines()

# count lines of code of file entered by user via the command line argument
def lines():
    # confirm only one command argument was given
    one_arg()
    # confirm that the file exists and read the file and store its contents in a var
    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File not found")

    # remove comments and empty lines
    code_lines = remove_comments_empty(lines)
    # Count remaining lines
    print(len(code_lines))

def one_arg():
    # confirm only one command argument was given
    if len(sys.argv) > 2:
        sys.exit("Too many command line arguments one argument expected")
    elif len(sys.argv) < 2:
        sys.exit("Too few command line arguments one argument expected")

# remove comments and empty lines
def remove_comments_empty(lines):
    code_lines = []
    for line in lines:
        line = line.strip()
        if line.startswith("#") or line == "":
            pass
        else:
            code_lines.append(line)
    return code_lines

if __name__ == "__main__":
    main()