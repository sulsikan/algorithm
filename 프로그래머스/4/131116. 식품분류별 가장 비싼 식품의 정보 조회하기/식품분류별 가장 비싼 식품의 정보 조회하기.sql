with Maxprice as (
    select CATEGORY, max(PRICE) as MAX_PRICE
    from FOOD_PRODUCT
    where CATEGORY in ('과자','국','김치','식용유')
    group by CATEGORY
)

select fp.CATEGORY, mp.MAX_PRICE, fp.PRODUCT_NAME
from FOOD_PRODUCT fp 
join Maxprice mp 
  on fp.CATEGORY = mp.CATEGORY 
  and fp.PRICE = mp.MAX_PRICE
order by MAX_PRICE desc;
