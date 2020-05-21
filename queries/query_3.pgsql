-- Teachers employed after date 2015-09-01 --
SELECT
    teacher_id AS id,
    surname,
    name,
    employment_date
FROM
    teachers
WHERE
    employment_date >= '2015-09-01'
ORDER BY
    employment_date
