import sys
import heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())

    max_heap = []
    min_heap = []
    visited = [False] * K

    for i in range(K):
        cmd, n = input().split()
        n = int(n)

        if cmd == 'I':
            heapq.heappush(max_heap, (-n, i))
            heapq.heappush(min_heap, (n, i))
            visited[i] = True

        elif cmd == 'D':
            if n == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
                    
            else:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
            
    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')
        