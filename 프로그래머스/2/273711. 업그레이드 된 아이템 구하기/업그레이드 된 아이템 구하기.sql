select 
    c.item_id, 
    c.item_name, 
    c.rarity
from item_info p
join item_tree t on p.item_id = t.parent_item_id
join item_info c on t.item_id = c.item_id
where p.rarity = 'RARE'
order by item_id desc;

# 과정 서술
# 아이템 정보는 item_info에만 존재하고 아이템 관계 정보는 item_tree에만 존재합니다.
# 부모 아이템 정보(ITEM_INFO) → 업그레이드 관계(ITEM_TREE) → 자식 아이템 정보(ITEM_INFO) 순서로 테이블을 연결해야 합니다.
# 이 과정에서 ITEM_INFO를 부모와 자식 역할로 두 번 사용하므로, 각 역할을 p(parent), c(child) 별칭으로 구분해 조인합니다.
# INNER JOIN은 업그레이드 관계가 실제로 존재하는 경우에만 결과가 생성되므로, “RARE 아이템 중 업그레이드된(자식이 있는) 아이템만” 정확히 추출할 수 있습니다.