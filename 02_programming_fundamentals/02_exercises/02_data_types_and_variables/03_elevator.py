num_people = int(input())
capacity = int(input())

people_left = num_people
counter_courses = 0

while people_left > 0:
    people_left -= capacity
    counter_courses += 1

print(counter_courses)
