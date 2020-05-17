-- GPA of students --
SELECT
    students.student_id,
    surname,
    name,
    TO_CHAR(AVG(grade), '9.9') as gpa
FROM
    students
    INNER JOIN grades ON grades.student_id = students.student_id
GROUP BY
    students.student_id
ORDER BY
    student_id
