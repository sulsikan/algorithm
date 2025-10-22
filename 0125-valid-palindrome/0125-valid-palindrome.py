class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 모두 lowercase로 변환
        s = s.lower()
        # 공백 제거
        s = re.sub('[^a-z0-9]', '', s)
        # 슬라이싱으로 값 비교
        return s == s[::-1]

        