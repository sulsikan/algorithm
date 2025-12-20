select count(*) as count
from ecoli_data
where genotype & b'0101' <> 0 and genotype & b'0010' = 0