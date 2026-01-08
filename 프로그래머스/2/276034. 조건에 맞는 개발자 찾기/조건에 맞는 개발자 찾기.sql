select distinct d.id, d.email, d.first_name, d.last_name
from developers d
join skillcodes s
  on d.skill_code & s.code > 0 
where s.name in ('Python', 'C#')
order by id

# 과정 설명
# 개발자의 보유 스킬이 비트 마스크 형태로 저장되어있어, 단순 문자열 비교가 아닌 AND 비트 연산으로 개발자 테이블과 스킬코드 테이블을 조인했습니다.
# Python 또는 C# 스킬을 가진 개발자만 조회하기 위해 해당 스킬 이름으로 필터링하고, 하나의 개발자가 여러 스킬을 가질 경우 발생하는 중복을 제거하기 위해 DISTINCT를 사용했습니다.