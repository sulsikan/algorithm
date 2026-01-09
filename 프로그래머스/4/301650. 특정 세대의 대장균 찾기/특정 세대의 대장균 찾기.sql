select 3gen.id
from ecoli_data 1gen
join ecoli_data 2gen on 1gen.id = 2gen.parent_id
join ecoli_data 3gen on 2gen.id = 3gen.parent_id
WHERE 1gen.parent_id IS NULL
ORDER BY 3gen.id ASC

# 세대 관계는 PARENT_ID가 부모 개체의 ID를 참조하는 구조이므로, 동일한 테이블(ECOLI_DATA)을 세대별 역할로 구분하여 셀프 조인을 수행했습니다.
# 먼저 gen1을 1세대로 두고 gen1.PARENT_ID IS NULL 조건을 적용해 시작점을 “최초 개체”로 고정했습니다. 
# 이후 gen2.PARENT_ID = gen1.ID 조건으로 1세대의 자식(2세대)을 연결하고, gen3.PARENT_ID = gen2.ID 조건으로 2세대의 자식(3세대)을 연결하여 정확히 “1세대 → 2세대 → 3세대” 경로만 추출했습니다.
# 최종적으로 3세대에 해당하는 개체의 ID만 선택하여 문제 요구사항에 따라 오름차순으로 정렬해 출력했습니다.