with TOTAL_ORDERs as (
    select F.FLAVOR, sum(F.TOTAL_ORDER + J.TOTAL_ORDER) AS TOTAL_ORDER
    from FIRST_HALF F
    join JULY J
      on F.FLAVOR = J.FLAVOR
    group by F.FLAVOR
    ORDER BY TOTAL_ORDER DESC
)
select FLAVOR
from total_orders
limit 3;