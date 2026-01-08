-- IS NOT NULL
SELECT MEMBER_ID, MEMBER_NAME, GENDER, date_format(DATE_OF_BIRTH, '%Y-%m-%d') as date_of_birth
from MEMBER_PROFILE
where month(DATE_OF_BIRTH) = 03 and GENDER='W' and TLNO is not null
order by member_id asc;