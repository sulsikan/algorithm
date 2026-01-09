select year(DIFFERENTIATION_DATE) as year, max(SIZE_OF_COLONY) over(partition by year(DIFFERENTIATION_DATE)) - SIZE_OF_COLONY as year_dev, id 
from ECOLI_DATA
order by year, year_dev

# 행 수를 그대로 유지하기 위해 윈도우 함수를 이용하여 max 값을 구했습니다.