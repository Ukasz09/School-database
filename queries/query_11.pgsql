-- Sum of work hours in week for every teacher --
CREATE VIEW sum_of_hours_teachers AS
SELECT
    teachers.teacher_id,
    name,
    surname,
    COALESCE(SUM(hours_per_week), 0) AS sum_of_hours_weekly
FROM
    teachers
    LEFT JOIN teaching ON teaching.teacher_id = teachers.teacher_id
GROUP BY
    teachers.teacher_id
ORDER BY
    sum_of_hours_weekly DESC
