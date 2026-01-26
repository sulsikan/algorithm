import sys
input = sys.stdin.readline

N = int(input())

N_arr = list(str(N))
numbers = []
answer = 0
cnt = 0

for num in range(10):
    numbers.append(N_arr.count(str(num)))

if numbers[6] > numbers[9]:
    cnt = numbers[6] - numbers[9]
    numbers[6] = (cnt+1) // 2
    print(max(numbers[9] + numbers[6], max(numbers)))

elif numbers[6] < numbers[9]:
    cnt = numbers[9] - numbers[6]
    numbers[9] = (cnt+1) // 2
    print(max(numbers[9] + numbers[6], max(numbers)))
else:
    print(max(numbers))