number_of_pages = int(input())
pages_per_hour = int(input())
number_of_days = int(input())
needed_hours = number_of_pages / pages_per_hour
hours_per_day = needed_hours / number_of_days
#hours_per_day = needed_hours // number_of_days - Това закръгля числото към по-малкото.
print(int(hours_per_day))
