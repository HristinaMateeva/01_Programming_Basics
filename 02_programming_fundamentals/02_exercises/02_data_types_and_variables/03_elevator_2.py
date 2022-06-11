num_people = int(input())
capacity = int(input())

full_courses = num_people // capacity
left_people = num_people % capacity

if left_people > 0:
    full_courses += 1
print(f"{full_courses}")
