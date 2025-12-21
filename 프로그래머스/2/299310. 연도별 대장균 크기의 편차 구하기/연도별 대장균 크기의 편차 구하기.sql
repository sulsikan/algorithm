select year(DIFFERENTIATION_DATE) year, max(SIZE_OF_COLONY) over (partition by year(DIFFERENTIATION_DATE))- SIZE_OF_COLONY year_dev, id
from ecoli_data
order by year, year_dev