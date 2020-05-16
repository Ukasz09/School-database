-- Students from class II, whose come from city beginning with [D-K] --

SELECT
    student_id AS id,
    students.name,
    students.surname,
    cities.name AS city_name
FROM
    students
    INNER JOIN classes ON students.class_id = classes.class_id
    INNER JOIN cities ON students.residence_location = cities.city_id
WHERE
    classes.class_number LIKE 'II'
    AND cities.name SIMILAR TO '[D-K]%'
ORDER BY
    students.surname,
    students.name
