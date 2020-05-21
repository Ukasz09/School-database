-- Teachers earning with extras (prize=0.2*hourly_rate*total_hours) --
SELECT
    teachers.teacher_id,
    teachers.surname,
    teachers.name,
    TO_CHAR(SUM(sum_of_hours_weekly * hourly_rate), '999990.00') AS month_salary,
    TO_CHAR(SUM(sum_of_hours_weekly * hourly_rate) * 0.2, '999990.00') AS extras,
    TO_CHAR(SUM(sum_of_hours_weekly * hourly_rate) * 0.2 + SUM(sum_of_hours_weekly * hourly_rate), '999990.00') AS total_salary
FROM
    teachers
    LEFT JOIN sum_of_hours_teachers AS hours ON teachers.teacher_id = hours.teacher_id
GROUP BY
    teachers.teacher_id
ORDER BY
    total_salary DESC
