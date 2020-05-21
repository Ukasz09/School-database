-- Return middle row of grades sorted in ascending order by date --
SELECT
    *
FROM
    grades
ORDER BY
    insertion_date OFFSET (
        SELECT
            (COUNT(student_id) - 1) / 2 FROM grades)
    ROWS FETCH FIRST 1 ROW ONLY
