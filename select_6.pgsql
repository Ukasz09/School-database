-- All students with grades --
SELECT
    grades.student_id AS id,
    students.surname,
    students.name,
    grade,
    subjects.name
FROM
    grades
    INNER JOIN students ON students.student_id = grades.student_id
    INNER JOIN subjects ON subjects.subject_id = grades.subject_id
ORDER BY
    grades.student_id
