-- Check if student has any grades in class register --
CREATE FUNCTION has_any_grades (id_of_student integer)
    RETURNS bool
    AS $$
BEGIN
    RETURN id_of_student IN (
        SELECT
            student_id
        FROM
            grades);
END;
$$
LANGUAGE plpgsql;

