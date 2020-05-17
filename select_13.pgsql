-- Math teachers --
SELECT
    teachers.teacher_id,
    teachers.name,
    surname,
    hours_per_week
FROM
    teaching
    INNER JOIN teachers ON teachers.teacher_id = teaching.teacher_id
    INNER JOIN subjects ON subjects.subject_id = teaching.subject_id
WHERE
    subjects.name = 'Math'
ORDER BY
    hours_per_week DESC
