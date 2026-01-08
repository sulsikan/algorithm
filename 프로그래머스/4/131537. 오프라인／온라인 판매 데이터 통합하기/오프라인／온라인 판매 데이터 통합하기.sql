select 
    date_format(sales_date, '%Y-%m-%d') as sales_date, 
    product_id, 
    user_id, 
    sales_amount
from online_sale
where date_format(sales_date, '%Y-%m') = '2022-03'

union all

select
    date_format(sales_date, '%Y-%m-%d') as sales_date, 
    product_id,
    null as user_id,
    sales_amount
from offline_sale
where date_format(sales_date, '%Y-%m') = '2022-03'

order by sales_date, product_id, user_id;

# 과정 서술
# 본 문제는 2022년 3월의 판매기록을 온라인 판매 테이블과 오프라인 판매 테이블에서 조회한 뒤 동일한 컬럼 구조로 하나의 결과 집합으로 합치는 것이 핵심입니다.
# 두 테이블은 서로 매칭되는 관계 (1:1, 1:N)이 아닌 각각 독립적인 이력을 가진 테이블로, join으로 결합하게되면 판매 데이터가 불필요하게 곱해지거나 잘못 매칭될 수 있습니다. 따라서 두 테이블을 결합하는 join이 아니라 연결시키는 union all을 사용하여 행을 그대로 이어 붙였습니다.
# 먼저 문제 요구사항에 맞게 각 테이블에서 sales_date를 2022년 3월인 데이터들만 필터링했습니다.
# online_sale 테이블은 user_id가 존재하니 그대로 출력하고, offline_sale 테이블은 문제 요구 사항에 따라 user_id 컬럼을 null 로 고정해 스키마를 통일시켰습니다.
# 마지막으로 결과를 판매 날짜 오름차순, 상품 ID 오름차순, USER_ID 오름차순으로 정렬하여 문제에서 요구한 출력 순서를 만족했습니다.