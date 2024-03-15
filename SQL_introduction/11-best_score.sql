-- lists all records with a score more than or equal to 10 on second_table --
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
