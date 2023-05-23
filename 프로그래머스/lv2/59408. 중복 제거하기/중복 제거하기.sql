-- 코드를 입력하세요
# SELECT distinct COUNT(NAME)  FROM ANIMAL_INS WHERE NAME is not NULL
select count(distinct name) from ANIMAL_INS;