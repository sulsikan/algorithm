class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 문자와 숫자 구분
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # letters 문자 -> identifier 순으로 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))  # 자동으로 x가 원소로 잡힘

        return letters + digits
        
'''
1. 아이디어
- 문자와 숫자를 구분한다. 로그 자체는 일단 모두 str로 되어있을 것임. 그래서 isdigit()을 이용해서 판별
- 숫자로그는 digits, 문자로그는 letters에 추가
- 먼저 letters를 정렬
- 숫자는 나중에 그대로 이어붙인다.

'''