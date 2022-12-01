-- Script that lists number of records with same score in second_table
-- Database name will be passed as argument
SELECT score, COUNT(score)
FROM second_table
GROUP BY score
