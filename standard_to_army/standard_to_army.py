import sys
import re

def main():
    print(convert(input("Please input your working hours: ")))

#Converts 12am format to 24h 
def convert(s):
    # confirm the correct format was given
    if time := re.search("([1-2]?[0-9](?::[0-5][0-9])?) ?(am|pm) to ([1-2]?[0-9](?::[0-5][0-9])?) ?(am|pm)", s, re.IGNORECASE):
        #Get start and hour 
        start = time.group(1)
        start_ap = time.group(2)
        end = time.group(3)
        end_ap = time.group(4)
        start = am_pm(start, start_ap)
        end = am_pm(end, end_ap)
        start_to_end = str(start) + " to " + str(end)
        return start_to_end
    else:
        return "Please input either one of the following formats 9:00 AM to 5:00 PM or 9 AM to 5 PM"
    
# adds turns pm to military time and adds zeros before single digits
def am_pm(time, amPm):
    # if time is am just check if the hour is 12 if it is than change houre to 00:00
    if "am" in amPm:
        hour = time.split(":")[0]
        hour_format = hour
        if "12" in hour:
            hour_format = "0"
        time = time.replace(hour, hour_format)
        hour = hour_format
    else:
        hour = time.split(":")[0]
        # if 12 is not in hour add 12 to hour
        if "12" not in hour:
            hour_format  = (int(hour)+ 12)
            time = time.replace(hour, str(hour_format))
            hour = hour_format

    # if hour is a single digit add a zero to the begining
    if int(hour) < 10:
        time = "0" + time
    try:
    # check to see if the user inputed the mins if not add :00 for the mins
        min = time.split(":")[1]
    except IndexError:
        time = time + ":00"
    return time

if __name__ == "__main__":
    main()
