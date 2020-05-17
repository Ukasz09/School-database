-- GPA of students all studetns (0.0 when no grades for student) --
SELECT
    students.student_id,
    surname,
    name,
    COALESCE(TO_CHAR(AVG(grade), '9.99'), '0.00') AS gpa
FROM
    students
    LEFT JOIN grades ON grades.student_id = students.student_id
GROUP BY
    students.student_id
ORDER BY
    student_id
