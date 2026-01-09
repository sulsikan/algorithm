-- 윈도우 함수를 사용해야 함
select 
    year(os.SALES_DATE) as year, 
    month(os.SALES_DATE) as month, 
    ui.GENDER, 
    count(distinct ui.user_id) as users
from USER_INFO ui
join ONLINE_SALE os 
  on ui.USER_ID= os.USER_ID
where ui.gender is not null
group by year(os.SALES_DATE), month(os.SALES_DATE), ui.GENDER
order by year(os.SALES_DATE), month(os.SALES_DATE), ui.GENDER