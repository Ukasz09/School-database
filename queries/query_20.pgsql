-- Creating copy of teachers table, where year of teacher employment_date is less than 1990 --
CREATE TABLE archieve AS
SELECT
    *
FROM
    teachers
WHERE
    EXTRACT('year' FROM employment_date) <= 1990;

-- Create copy of all values of students table --
CREATE TABLE students_archieve AS TABLE students
