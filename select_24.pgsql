-- Specific teacher with all given grades --
SELECT
    t.teacher_id,
    t.name AS teacher_name,
    t.surname AS teacher_surname,
    g.grade,
    g.subject_id,
    sub.name AS subject,
    stud.student_id,
    stud.name AS student_name,
    stud.surname AS student_surname,
    g.insertion_date AS date
FROM
    teachers AS t
    INNER JOIN grades AS g ON g.teacher_id = t.teacher_id
    INNER JOIN subjects AS sub ON sub.subject_id = g.subject_id
    INNER JOIN students AS stud ON stud.student_id = g.student_id
WHERE
    t.name = 'Damon'
    AND t.surname = 'Baker'
ORDER BY
    g.insertion_date DESC
