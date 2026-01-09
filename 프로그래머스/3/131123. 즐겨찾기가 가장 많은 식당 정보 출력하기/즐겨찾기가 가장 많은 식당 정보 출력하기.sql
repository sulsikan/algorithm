with Favorite_rest as (
    select FOOD_TYPE, max(FAVORITES) as FAVORITES
    from REST_INFO
    group by FOOD_TYPE
)
select ri.FOOD_TYPE, ri.REST_ID, ri.REST_NAME, fs.FAVORITES
from REST_INFO ri
join Favorite_rest fs on ri.FOOD_TYPE=fs.FOOD_TYPE and ri.FAVORITES = fs.FAVORITES
order by FOOD_TYPE desc;