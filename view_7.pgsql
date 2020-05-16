-- Full complete students grades view --
SELECT
    students.name || ' ' || surname || ' ' || students.student_id AS student,
    subjects.name,
    grade,
    grade_to_words (grade) AS grade_in_words
FROM
    grades
    INNER JOIN students ON students.student_id = grades.student_id
    INNER JOIN subjects ON subjects.subject_id = grades.subject_id
ORDER BY
    student
