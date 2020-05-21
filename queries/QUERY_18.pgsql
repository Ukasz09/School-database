-- Teachers who are not tutor --
SELECT
    teacher_id,
    name,
    surname
FROM
    teachers
    LEFT JOIN classes ON tutor_id = teacher_id
WHERE
    tutor_id IS NULL
ORDER BY
    teacher_id
