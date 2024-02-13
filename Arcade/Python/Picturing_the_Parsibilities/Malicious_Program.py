from datetime import datetime, timedelta

def solution(curDate, changes):
    # Parse the current date
    curDate = datetime.strptime(curDate, "%d %b %Y %H:%M:%S")

    # Calculate the new date
    try:
        newYear = curDate.year + changes[2]
        newMonth = curDate.month + changes[1]
        newDay = curDate.day + changes[0]
        newHour = curDate.hour + changes[3]
        newMinute = curDate.minute + changes[4]
        newSecond = curDate.second + changes[5]

        # Check if the new date components are valid
        if not(1 <= newMonth <= 12 and 0 <= newHour < 24 and 0 <= newMinute < 60 and 0 <= newSecond < 60):
            raise ValueError

        newDate = datetime(newYear, newMonth, newDay, newHour, newMinute, newSecond)
    except ValueError:
        # If the new date is not valid, return the original date
        return curDate.strftime("%d %b %Y %H:%M:%S")

    return newDate.strftime("%d %b %Y %H:%M:%S")
