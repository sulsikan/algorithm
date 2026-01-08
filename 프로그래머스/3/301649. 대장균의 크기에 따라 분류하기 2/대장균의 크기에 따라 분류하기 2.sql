with ranked as (
    select 
        id,
        ntile(4) over (order by size_of_colony desc) as grp
    from ecoli_data
)
select 
    id, 
    case grp
        when 1 then 'CRITICAL'
        when 2 then 'HIGH'
        when 3 then 'MEDIUM'
        else 'LOW'
    end as COLONY_NAME
from ranked
order by id asc;

# 본 문제는 대장균의 SIZE_OF_COLONY를 내림차순으로 정렬한 뒤, 전체 데이터를 25% 단위로 4개 구간으로 분할하여 각 구간에 CRITICAL/HIGH/MEDIUM/LOW 등급을 부여하는 문제입니다.
# 이를 위해 정렬된 순서 기준으로 데이터를 동일 비율로 나누는 윈도우 함수 NTILE(4) OVER (ORDER BY SIZE_OF_COLONY DESC)를 사용해 각 행이 속한 분위(1~4)를 계산했습니다.
# 계산된 분위 값에 대해 CASE로 등급명을 매핑하여 COLONY_NAME을 생성하고, 최종적으로 문제 요구에 따라 ID 기준 오름차순으로 정렬해 출력했습니다.