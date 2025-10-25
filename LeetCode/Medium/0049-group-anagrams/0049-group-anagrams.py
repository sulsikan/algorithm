class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 애나그램 구분... 전혀 모르겠음
        # 애나그램 판단하는 가장 간단한 방법 : 정렬하여 비교
        # 단어 쪼개서 정렬해서 애나그램인 단어를 찾기

        # key가 없어도 항상 디폴트로 키 생성해주는 딕셔너리 초기화
        anagrams = collections.defaultdict(list)

        for word in strs:
            # 정렬해서 딕셔너리 추가
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())

'''
word = "eat"
sorted(word) → ['a', 'e', 't']
''.join(sorted(word)) → "aet"

dict_values 객체는 단순히 "참조용 뷰"라서,
리스트 연산(인덱싱, 슬라이싱 등)을 직접 사용할 수 없다
그래서 결과를 일반 리스트처럼 다루기 위해 list()로 한 번 감싸준다.
'''