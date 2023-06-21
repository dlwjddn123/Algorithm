month_day = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
m, d = map(int, input().split())
dayOfTheWeek = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
day = (month_day[m] + d) % 7
print(dayOfTheWeek[day-1])
