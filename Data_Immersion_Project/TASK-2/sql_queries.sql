 1. Top categories
SELECT column_name, COUNT(*) 
FROM table_name
GROUP BY column_name
ORDER BY COUNT(*) DESC
LIMIT 5;

2. Total records
SELECT COUNT(*) FROM table_name;

3. Missing values check
SELECT COUNT(*) 
FROM table_name
WHERE column_name IS NULL;

4. Average analysis
SELECT AVG(numeric_column) 
FROM table_name;

5. Trend analysis
SELECT column_name, COUNT(*)
FROM table_name
GROUP BY column_name;

6. Join example (theory)
SELECT *
FROM table1
JOIN table2 ON table1.id = table2.id;