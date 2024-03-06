jobs = {
    "Каменщик": 1,
    "Программист": 1,
    "Строитель": 2,
}
a = int(input())
for t in jobs:
    if jobs[t] == a:
        print(t)