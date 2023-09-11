import re
import sys

def main():
    print(validate(sys.argv[1]))



def validate(ip):
    if re.match(r"^([0-9]{1,2}|[1][0-9]{2}|[2][0-4][0-9]|[2][0-5][0-5])\.([0-9]{1,2}|[1][0-9]{2}|[2][0-4][0-9]|[2][0-5][0-5])\.([0-9]{1,2}|[1][0-9]{2}|[2][0-4][0-9]|[2][0-5][0-5])\.([0-9]{1,2}|[1][0-9]{2}|[2][0-4][0-9]|[2][0-5][0-5])$", ip):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()