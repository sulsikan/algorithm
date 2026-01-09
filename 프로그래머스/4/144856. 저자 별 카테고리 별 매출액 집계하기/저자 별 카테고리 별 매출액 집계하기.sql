select ar.AUTHOR_ID, ar.AUTHOR_NAME, bk.CATEGORY, sum(bs.SALES * bk.PRICE) as TOTAL_SALES
from BOOK bk
join AUTHOR ar on bk.AUTHOR_ID = ar.AUTHOR_ID
join BOOK_SALES bs on bk.BOOK_ID = bs.BOOK_ID
-- 2022년 1월 BOOK_SALES
where date_format(bs.SALES_DATE, '%Y-%m') = '2022-01'
-- AUTHOR_ID, CATEGORY별
group by AUTHOR_ID, CATEGORY
-- total_sales = 판매량 * 판매가
order by AUTHOR_ID, CATEGORY desc;


# select ar.AUTHOR_ID, ar.AUTHOR_NAME, bk.CATEGORY, (bs.SALES * bk.PRICE) as TOTAL_SALES
# from (
#     select *
#     from BOOK_SALES
#     where date_format(SALES_DATE, '%Y-%m') = '2022-01'
# ) bs
# join BOOK bk on bk.BOOK_ID = bs.BOOK_ID
# join AUTHOR ar on bk.AUTHOR_ID = ar.AUTHOR_ID
# group by AUTHOR_ID, CATEGORY
# order by AUTHOR_ID, CATEGORY desc;