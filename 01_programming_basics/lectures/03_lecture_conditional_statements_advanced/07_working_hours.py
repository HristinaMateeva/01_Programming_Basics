hour = int(input())
day = input()

# работното време на офисът е от 10-18 часа, от понеделник до събота включително

is_working_day = day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday"
if hour >= 10 and hour <= 18:
    if is_working_day:
        print("open")

if day == "Sunday" or hour < 10 or hour > 18:
    print("closed")
