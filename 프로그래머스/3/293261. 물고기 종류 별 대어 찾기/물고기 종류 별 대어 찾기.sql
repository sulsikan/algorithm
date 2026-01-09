WITH MaxLengthByType AS (
    SELECT
        FISH_TYPE,
        MAX(LENGTH) AS MaxLength
    FROM FISH_INFO
    GROUP BY FISH_TYPE
)
SELECT
    FI.ID,
    FN.FISH_NAME,
    FI.LENGTH
FROM MaxLengthByType M
JOIN FISH_INFO FI
    ON FI.FISH_TYPE = M.FISH_TYPE
   AND FI.LENGTH = M.MaxLength
JOIN FISH_NAME_INFO FN
    ON FI.FISH_TYPE = FN.FISH_TYPE
ORDER BY FI.ID ASC;


# 물고기 종류별로 가장 큰 물고기의 정보를 조회하기 위해, 먼저 동일한 종류(FISH_TYPE)에 속한 물고기들의 최대 길이(MAX(LENGTH))를 구했습니다. 이 최대 길이값과 실제 물고기 길이(FISH_INFO.LENGTH)가 일치하는 행을 서브쿼리로 필터링하여, 해당 종의 가장 큰 물고기 한 마리만 선택했습니다. 이후 물고기 이름 정보가 담긴 FISH_NAME_INFO 테이블을 FISH_TYPE으로 조인해 이름을 붙였으며, 최종 결과는 문제 요구대로 ID 오름차순 정렬로 출력했습니다.