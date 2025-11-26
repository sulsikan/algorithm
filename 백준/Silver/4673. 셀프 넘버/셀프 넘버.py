def d(n):
    return n + sum(map(int, str(n)))

results = set()
for i in range(1, 10001):
    results.add(d(i))
for j in range(1, 10001):
    if j not in results:
        print(j)