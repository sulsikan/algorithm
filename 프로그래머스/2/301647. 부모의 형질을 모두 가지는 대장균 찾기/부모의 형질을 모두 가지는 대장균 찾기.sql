SELECT c.ID, c.GENOTYPE, p.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA c
JOIN ECOLI_DATA p 
  ON c.PARENT_ID = p.ID
WHERE (c.GENOTYPE & p.GENOTYPE) = p.GENOTYPE
ORDER BY ID ASC;

# 부모–자식 관계를 PARENT_ID 기준으로 셀프 조인하고,
# 형질이 비트 마스크로 저장되어 있으므로 비트 AND 연산을 사용해
# 자식이 부모의 형질을 모두 포함하는 경우만 필터링했습니다.