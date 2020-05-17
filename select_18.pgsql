-- Students with amount of subjects from which obtained at least one grade --
WITH students_with_unique_subjects AS (
    SELECT
        s.student_id,
        COUNT(g.subject_id) AS grades_from_one_subj
    FROM
        students AS s
        LEFT JOIN grades AS g ON s.student_id = g.student_id
    GROUP BY
        s.student_id,
        g.subject_id
    ORDER BY
        s.student_id
)
SELECT
    s.student_id AS id,
    name,
    surname,
    COUNT(grades_from_one_subj) AS subjects_with_grades
FROM
    students AS s
    LEFT JOIN students_with_unique_subjects AS s_uniq ON s.student_id = s_uniq.student_id
GROUP BY
    s.student_id
ORDER BY
    s.student_id
