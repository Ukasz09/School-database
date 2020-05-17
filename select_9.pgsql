-- Students from Hollywod and New Berlin --
SELECT
    student_id,
    students.name,
    surname,
    cities.name AS residence_location_city
FROM
    students
    INNER JOIN cities ON city_id = residence_location
WHERE
    cities.name SIMILAR TO 'Hollywood|New Berlin'
ORDER BY
    students.student_id
