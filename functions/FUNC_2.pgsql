-- Calculating total teacher salary --
CREATE FUNCTION total_salary (id_of_teacher integer)
    RETURNS float
    AS $$
DECLARE
    result float;
BEGIN
    SELECT
        SUM(sum_of_hours_weekly * hourly_rate) * 0.2 + SUM(sum_of_hours_weekly * hourly_rate) INTO result
    FROM
        teachers
    LEFT JOIN sum_of_hours_teachers AS hours ON teachers.teacher_id = hours.teacher_id
WHERE
    teachers.teacher_id = id_of_teacher
GROUP BY
    teachers.teacher_id;
    RETURN result;
END;
$$
LANGUAGE plpgsql;

