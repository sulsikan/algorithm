
-- 완료된 중고거래의 총금액이 70만원 이상인 사람
-- STATUS = 'DONE' and sum(PRICE) >= 700000
with Done_user_higher_700000 as (
    select b.WRITER_ID, sum(b.PRICE) as TOTAL_SALES
    from USED_GOODS_BOARD b
    join USED_GOODS_USER u on b.WRITER_ID = u.USER_ID
    where b.STATUS = 'DONE'
    group by b.WRITER_ID
    having sum(PRICE) >= 700000
)
select d.WRITER_ID, u.NICKNAME, d.TOTAL_SALES
from Done_user_higher_700000 d
join USED_GOODS_USER u on d.WRITER_ID = u.USER_ID
order by TOTAL_SALES asc;