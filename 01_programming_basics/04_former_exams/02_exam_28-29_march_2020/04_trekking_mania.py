number_groups = int(input())

climbers_musala = 0
climbers_mon_blanc = 0
climbers_kilimandjaro = 0
climbers_k2 = 0
climbers_everest = 0
total_people = 0

for num in range(1, number_groups + 1):
    number_people = int(input())
    if number_people <= 5:
        climbers_musala += number_people
        total_people += number_people
    elif 6 <= number_people <= 12:
        climbers_mon_blanc += number_people
        total_people += number_people
    elif 13 <= number_people <= 25:
        climbers_kilimandjaro += number_people
        total_people += number_people
    elif 26 <= number_people <= 40:
        climbers_k2 += number_people
        total_people += number_people
    elif number_people >= 41:
        climbers_everest += number_people
        total_people += number_people

percent_musala = climbers_musala / total_people * 100
percent_mon_blanc = climbers_mon_blanc / total_people * 100
percent_kilimandjaro = climbers_kilimandjaro / total_people * 100
percent_k2 = climbers_k2 / total_people * 100
percent_everest = climbers_everest / total_people * 100

print(f"{percent_musala:.2f}%")
print(f"{percent_mon_blanc:.2f}%")
print(f"{percent_kilimandjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")
