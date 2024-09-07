def timeConversion(time_str):
    # Write your code here
    time_period = time_str[-2:]
    hours = time_str[0:2]
    mints = time_str[3:5]
    seconds = time_str[6:8]
    if time_period == "AM" and hours == "12":
        hours = "00"
    elif time_period == "PM" and hours != "12":
        hours = str(int(hours) + 12)
    print(f"{hours}:{mints}:{seconds}")

    return f"{hours}:{mints}:{seconds}"


time_str = "12:45:54PM"
timeConversion(time_str)
