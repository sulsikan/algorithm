n = int(input())

work_time_table = {}
for _ in range(n):
    name, state = input().split()
    if state == 'enter':
        work_time_table[name] = state
    else:
        del work_time_table[name]

least_people_arr = []
for name in work_time_table:
    least_people_arr.append(name)
least_people_arr.sort(reverse = True)

for name in least_people_arr:
    print(name)