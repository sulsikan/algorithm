'''
<문제>
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

<입력>  
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

<출력>
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
'''
import sys  
input = sys.stdin.readline

word = input().strip().upper()    # 대소문자 통일 (대문자로)
alphabet_count = {}

# 알파벳 개수 세기
for char in word:
    # 초깃값 설정
    if char in alphabet_count:
        alphabet_count[char] += 1
    else:
        alphabet_count[char] = 1

# 최대 빈도 계산
max_count = max(alphabet_count.values())

# 최대 빈도를 가진 알파벳 목록
max_alphabets = [ k for k, v in alphabet_count.items() if v == max_count]
# alphabet_count.items()는 딕셔너리의 (키, 값) 쌍을 튜플 형태로 묶은 반복 가능한 객체(iterable)를 반환

# 결과가 1일때만 출력
if len(max_alphabets) == 1:
    print(max_alphabets[0])
else:
    print('?')