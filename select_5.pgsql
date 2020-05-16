-- Teachers with seniority bigger or equal 20 years --
SELECT
    teacher_id,
    surname,
    name,
    employment_date,
    DATE_PART('year', AGE(employment_date)) AS seniority
FROM
    teachers
WHERE
    DATE_PART('year', AGE(employment_date)) >= 20
ORDER BY
    seniority DESC
