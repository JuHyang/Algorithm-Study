SELECT HOUR(DATETIME), COUNT (*)
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) >= 0 AND HOUR(DATETIME) <= 23
GROUP BY HOUR(DATETIME);