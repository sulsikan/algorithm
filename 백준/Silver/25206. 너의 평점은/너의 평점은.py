import sys
input = sys.stdin.readline

# initial setting
grade_list = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
score_list = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

tot_credit = 0  # 누적 단위수(sum 단위수)
tot_score = 0   # 누적 성적(sum 단위수 X 성적)

for _ in range(20):
    # 과목명, 단위수, 학점
    info = list(map(str, input().strip().split()))
    credit = float(info[1])
    # P/F 처리
    if info[2] == "P":
        continue
    else:
        idx = grade_list.index(info[2])
        score = score_list[idx]
        tot_credit += credit
        tot_score += (credit*score)

avg_score = float(tot_score/tot_credit)
print(avg_score)