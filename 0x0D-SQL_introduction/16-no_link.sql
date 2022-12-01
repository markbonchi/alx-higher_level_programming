-- Script that lists all records of second_table
-- Ignore rows without name value
-- Database name passed as argument
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC
