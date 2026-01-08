select p.id, ifnull(count(c.id), 0) as child_count
from ecoli_data p
left join ecoli_data c
  on p.id = c.parent_id
group by p.id
order by id asc

# 과정 서술
# 대장균 개체의 부모 자식 관계를 구하기 위해 id와 parent_id를 연결하여 셀프 조인을 진행했습니다. 이때 left 조인을 사용했는데, 이는 자식이 없는 대장균 개체가 있기 때문에 부모 id를 기준으로 사용했습니다.
# 부모 id 별로 자식 수를 세어주기 위해 p.id로 그룹화를 진행했고, 자식이 없는 대장균 개체의 자식 수를 0으로 출력하기 위해 ifnull을 이용했습니다.
