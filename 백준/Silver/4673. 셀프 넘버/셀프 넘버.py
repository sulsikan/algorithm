def self_number(x):
    num = list(str(x))
    result = 0
    for n in num:
        result += int(n)
    result += x
    return result

results = set()
for i in range(10001):
    results.add(self_number(i))
for j in range(10001):
    if j not in results:
        print(j)