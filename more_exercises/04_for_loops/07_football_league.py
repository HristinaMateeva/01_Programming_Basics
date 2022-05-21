stadium_capacity = int(input())
num_fans = int(input())

sector_a_fans = 0
sector_b_fans = 0
sector_v_fans = 0
sector_g_fans = 0

for i in range (1, num_fans + 1):
    sector = input()
    if sector == "A":
        sector_a_fans += 1
    elif sector == "B":
        sector_b_fans += 1
    elif sector == "V":
        sector_v_fans += 1
    elif sector == "G":
        sector_g_fans += 1

percent_sector_a = sector_a_fans / num_fans * 100
percent_sector_b = sector_b_fans / num_fans * 100
percent_sector_v = sector_v_fans / num_fans * 100
percent_sector_g = sector_g_fans / num_fans * 100
total_percent = num_fans / stadium_capacity * 100

print(f'{percent_sector_a:.2f}%')
print(f'{percent_sector_b:.2f}%')
print(f'{percent_sector_v:.2f}%')
print(f'{percent_sector_g:.2f}%')
print(f"{total_percent:.2f}%")
