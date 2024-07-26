-- 코드를 작성해주세요
WITH MAX_LENGTH_BY_TYPE AS (
    SELECT FISH_TYPE, FISH_NAME, MAX(LENGTH) AS LENGTH
    FROM FISH_INFO NATURAL JOIN FISH_NAME_INFO
    GROUP BY FISH_TYPE, FISH_NAME
)

SELECT ID, FISH_NAME, LENGTH 
FROM FISH_INFO NATURAL JOIN MAX_LENGTH_BY_TYPE;