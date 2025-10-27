class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        if not bank:
            return 0
        # 레이저의 개수 = [전 행에 있던 장치 * 다음 행에 있는 장치] 를 모두 더함
        # total = [cnt * cur_cnt] 반복하며 total에 추가
        cnt = 0
        total = 0
        for row in bank:
            # 리스트에서 1(장치) 개수 세기
            cur_cnt = row.count('1')
            if cur_cnt > 0:
                total += cnt * cur_cnt
                cnt = cur_cnt
        
        return total
