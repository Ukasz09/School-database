-- Union result of two tables: teachers and students together with occupation --
SELECT
    students.student_id AS id,
    students.surname,
    students.name,
    'Teacher' AS occupation
FROM
    students
UNION ALL
SELECT
    teachers.teacher_id,
    teachers.surname,
    teachers.name,
    'Student' AS occupation
FROM
    teachers
ORDER BY
    surname,
    name,
    id
