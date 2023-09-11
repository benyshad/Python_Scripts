import sys
import requests

def main():
    bitcoin()

def bitcoin():
    # check to make sure 1 argument was given and it is a digit
    if arg_checker(2) == False:
        sys.exit("Expected 1 argumnet. " + str(len(sys.argv)-1) + " were given.")
    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Unkown option. Please provide a number. ")
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = response.json()
    usd_rate = (response["bpi"]["USD"]["rate_float"]) * amount
    usd_rate = round(usd_rate, 2)
    print(f"${usd_rate:,.4f}")



# check that proper amounts of args are given
def arg_checker(n):
    if len(sys.argv) == n:
        return True
    else:
        return False

if __name__ == "__main__":
    main()