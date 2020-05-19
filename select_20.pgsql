-- For every surname, amount of students with the same surname --
SELECT
    surname,
    COUNT(student_id) AS students_with_this_surname_qty
FROM
    students
GROUP BY
    surname
ORDER BY
    students_with_this_surname_qty DESC
