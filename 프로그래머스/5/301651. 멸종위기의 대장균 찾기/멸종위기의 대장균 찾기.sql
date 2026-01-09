# 깊이를 알 수 없는 계층 구조를 띄고 있어서 WITH RECURSIVE(재귀 CTE)를 사용했습니다. 부모 ID = 자식 PARENT_ID 관계를 재귀적으로 따라가며 GENERATION을 1씩 증가시켜 모든 개체에 세대 값을 부여했습니다.
# 세대가 부여된 결과에서 자식이 없는 개체(leaf)만 구하기 위해 동일 CTE를 한 번 더 LEFT JOIN하여 자식이 매칭되지 않는(child.id IS NULL) 행만 필터링했고, 이를 GENERATION 기준으로 COUNT(*) 집계하여 세대별 leaf 개체 수를 계산했습니다. 마지막으로 세대 오름차순으로 정렬해 요구사항을 만족했습니다.

WITH RECURSIVE gen AS (
  -- 1세대: 부모가 없는 최초 개체
  SELECT
    id,
    parent_id,
    1 AS generation
  FROM ecoli_data
  WHERE parent_id IS NULL

  UNION ALL

  -- 다음 세대: 이전 세대의 id를 parent_id로 가지는 개체
  SELECT
    e.id,
    e.parent_id,
    g.generation + 1 AS generation
  FROM ecoli_data e
  JOIN gen g
    ON e.parent_id = g.id
)

SELECT
  COUNT(*) AS COUNT,
  g.generation AS GENERATION
FROM gen g
LEFT JOIN gen c
  ON c.parent_id = g.id
WHERE c.id IS NULL          -- 자식이 없는 개체만(leaf)
GROUP BY g.generation
ORDER BY g.generation ASC;
