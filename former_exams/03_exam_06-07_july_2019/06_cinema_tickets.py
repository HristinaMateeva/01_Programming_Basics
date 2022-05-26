command = input()

counter_student = 0
counter_standard = 0
counter_kid = 0
total_tickets_counter = 0

while command != "Finish":
    name_movie = command
    empty_seats = int(input())
    sold_tickets = 0
    total_tickets = empty_seats
    while empty_seats > 0:
        type_ticket = input()
        if type_ticket == "End":
            break
        elif type_ticket == "student":
            counter_student += 1
        elif type_ticket == "standard":
            counter_standard += 1
        elif type_ticket == 'kid':
            counter_kid += 1
        empty_seats -= 1
        sold_tickets += 1
        total_tickets_counter += 1
    percent_hall = sold_tickets / total_tickets * 100
    print(f"{name_movie} - {percent_hall:.2f}% full.")
    command = input()

percent_student = counter_student / total_tickets_counter * 100
percent_standard = counter_standard / total_tickets_counter * 100
percent_kid = counter_kid / total_tickets_counter * 100

print(f"Total tickets: {total_tickets_counter}")
print(f"{percent_student:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kid:.2f}% kids tickets.")
