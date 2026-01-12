def solution(n, w, num):
    # 오른쪽 왼쪽 번갈아 가며 2차원 배열에 택배상자를 쌓자
    # 각 열을 기준으로 배열을 만들어, 상자를 꺼낼 때 해당 열의 인덱스를 계산해서 꺼내자
    boxs = [[] for _ in range(w)]
    direction = 1
    box_num = 0
    # 1 ~ n까지 배열에 담기
    while box_num <= n:
        for i in range(0, w, direction) if direction == 1 else range(w-1, -1, -1):
            box_num += 1
            if box_num > n:
                break
            boxs[i].append(box_num)
        direction *= -1
    for row in boxs:
        if num in row:
            answer = len(row) - row.index(num)
    return answer