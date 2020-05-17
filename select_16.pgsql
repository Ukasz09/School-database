-- Teacher employed in month: may --
SELECT
    *
FROM
    teachers
WHERE
    DATE_PART('month', employment_date) = 5
ORDER BY
    teacher_id
