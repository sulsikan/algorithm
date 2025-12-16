-- 코드를 작성해주세요
select COUNT(*) as count from ECOLI_DATA
where genotype & 2 = 0 and genotype & 5 <> 0