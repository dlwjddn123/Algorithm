-- 코드를 작성해주세요

SELECT
    ED1.ID, ED1.GENOTYPE, ED2.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA AS ED1 LEFT JOIN ECOLI_DATA AS ED2 ON ED1.PARENT_ID = ED2.ID
WHERE ED1.GENOTYPE & ED2.GENOTYPE = ED2.GENOTYPE
ORDER BY ED1.ID;