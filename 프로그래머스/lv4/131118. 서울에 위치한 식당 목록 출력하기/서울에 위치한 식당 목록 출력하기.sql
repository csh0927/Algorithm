-- 코드를 입력하세요
SELECT i.REST_ID, i.REST_NAME, i.FOOD_TYPE, i.FAVORITES, i.ADDRESS, ROUND(AVG(r.REVIEW_SCORE),2) AS SCORE
FROM REST_INFO i, REST_REVIEW r
WHERE i.REST_ID = r.REST_ID 
GROUP BY r.REST_ID
HAVING i.ADDRESS LIKE '서울%'
ORDER BY SCORE DESC, i.FAVORITES DESC; 