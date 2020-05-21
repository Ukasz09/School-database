-- All greades for specific class symbol --
SELECT
    g.grade,
    g.insertion_date AS date,
    g.subject_id,
    sub.name AS subject_name,
    stud.student_id,
    stud.name AS student_name,
    stud.surname AS student_surname,
    t.teacher_id,
    t.name AS teacher_name,
    t.surname AS teacher_surname
FROM
    teachers AS t
    INNER JOIN grades AS g ON g.teacher_id = t.teacher_id
    INNER JOIN subjects AS sub ON sub.subject_id = g.subject_id
    INNER JOIN students AS stud ON stud.student_id = g.student_id
    INNER JOIN classes AS c ON c.class_id = stud.class_id
WHERE
    c.class_number = 'II'
    AND c.class_label = 'a'
ORDER BY
    g.insertion_date DESC
