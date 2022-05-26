num_groups = int(input())
total_people = 0
mount_musala = 0
mount_mont_blanc = 0
mount_kilimandjaro = 0
mount_k2 = 0
mount_everest = 0
for count in range(1, num_groups + 1):
    group_number_members = int(input())
    total_people += group_number_members
    if group_number_members <= 5:
       mount_musala += group_number_members
    elif 5 < group_number_members <= 12:
        mount_mont_blanc += group_number_members
    elif 12 < group_number_members <= 25:
        mount_kilimandjaro += group_number_members
    elif 25 < group_number_members <= 40:
        mount_k2 += group_number_members
    elif group_number_members > 40:
        mount_everest += group_number_members
mount_musala = mount_musala / total_people * 100
mount_mont_blanc = mount_mont_blanc / total_people * 100
mount_kilimandjaro = mount_kilimandjaro / total_people * 100
mount_k2 = mount_k2 / total_people * 100
mount_everest = mount_everest / total_people * 100

print(f"{mount_musala:.2f}%")
print(f"{mount_mont_blanc:.2f}%")
print(f"{mount_kilimandjaro:.2f}%")
print(f"{mount_k2:.2f}%")
print(f"{mount_everest:.2f}%")
