-- Add 'email' column to students
ALTER TABLE students
    ADD COLUMN email text UNIQUE;

-- Add default generated email to first 100 students --
WITH first_100_students AS (
    SELECT
        student_id
    FROM
        students
    ORDER BY
        student_id
    LIMIT 100)
UPDATE
    students
SET
    email = CONCAT(LOWER(name), '.', LOWER(surname), students.student_id, '@gmail.com')
FROM
    first_100_students
WHERE
    students.student_id = first_100_students.student_id;

