import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
jewelry = []
for _ in range(n):
    heapq.heappush(jewelry, list(map(int, input().split())))

bags = [int(input()) for _ in range(k)]
bags.sort()

heap = []
sum_value = 0
for bag in bags:
    while jewelry and bag >= jewelry[0][0]:
        heapq.heappush(heap, -heapq.heappop(jewelry)[1])
    if heap:
        sum_value -= heapq.heappop(heap)

print(sum_value)