SELECT
    id,
    case
        when size_of_colony <= 100 then 'LOW'
        when size_of_colony <= 1000 then 'MEDIUM'
        when size_of_colony > 1000 then 'HIGH'
    end as size
FROM ecoli_data
ORDER BY id asc;