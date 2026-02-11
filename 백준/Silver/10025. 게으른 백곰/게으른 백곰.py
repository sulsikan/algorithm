import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# (position, ice_amount) 형태로 모음
pos_to_ice = {}
for _ in range(n):
    ice_amount, position = map(int, input().split())
    pos_to_ice[position] = pos_to_ice.get(position, 0) + ice_amount  # 같은 위치면 누적

# 위치 기준으로 정렬된 리스트: [(position, total_ice), ...]
ice_points = sorted(pos_to_ice.items())

left = 0
current_window_sum = 0
max_window_sum = 0
max_distance = 2 * k  # [center-k, center+k] 범위의 길이 = 2k

for right in range(len(ice_points)):
    right_pos, right_ice = ice_points[right]
    current_window_sum += right_ice

    # 윈도우 조건: 가장 오른쪽 - 가장 왼쪽 위치가 2k 이하여야 함
    while ice_points[right][0] - ice_points[left][0] > max_distance:
        current_window_sum -= ice_points[left][1]
        left += 1

    if current_window_sum > max_window_sum:
        max_window_sum = current_window_sum

print(max_window_sum)
