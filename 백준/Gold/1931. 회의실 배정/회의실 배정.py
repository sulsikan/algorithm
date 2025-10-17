import sys

def main():
    N = int(sys.stdin.readline())
    meetings = []
    for _ in range(N):
        s, e = map(int, sys.stdin.readline().split())
        meetings.append((s,e))

    meetings.sort(key=lambda x: (x[1], x[0]))

    end = 0
    count = 0
    for s, e in meetings:
        if s >= end:
            count += 1
            end = e

    print(count)

if __name__ == "__main__":
    main()