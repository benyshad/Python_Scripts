from datetime import datetime

def main():
    print(seasons(input("Please Input Date As YYYY-MM-DD: ")))

# counts the min from between the date passed and the current date
def seasons(date):
    input_date = datetime.fromisoformat(date)
    today = datetime.today()
    today = today.replace(hour=0, minute=0, second=0, microsecond=0)

    # get the diffrence in days
    days_diff = today - input_date
    # return min
    return(days_diff.days * 24 * 60)

if __name__ == "__main__":
    main()