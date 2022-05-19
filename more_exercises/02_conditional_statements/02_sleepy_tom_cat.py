days_off = int(input())
time_days_off = days_off * 127
time_working_days = (365 - days_off) * 63
playing_time = time_days_off + time_working_days
norm = 30000
difference = abs(norm - playing_time)
hours = difference // 60
minutes = difference % 60

if playing_time > norm:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
elif playing_time <= norm:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
