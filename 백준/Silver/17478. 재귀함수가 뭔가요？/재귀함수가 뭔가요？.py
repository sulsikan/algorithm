N = int(input())

# 시작
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")

# 먼저 문장을 배열에 저장
the_start_sentence = '"재귀함수가 뭔가요?"'
lines = [
    '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.',
    '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.',
    '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
]
response = '"재귀함수는 자기 자신을 호출하는 함수라네"'
the_last_sentence = '라고 답변하였지.'

cnt = 0
# while 문으로 언제까지 재귀할 건지 지정
while cnt < N:
    print(the_start_sentence)
    print('\n'.join(lines))
    for i in range(len(lines)):
        lines[i] = '____' + lines[i]
    the_start_sentence = '____' + the_start_sentence
    response = '____' + response
    the_last_sentence = '____' + the_last_sentence
    cnt += 1

print(f"{the_start_sentence}\n{response}\n{the_last_sentence}")

while cnt > 0:
    the_last_sentence = the_last_sentence[4:]
    print(the_last_sentence)
    cnt -= 1