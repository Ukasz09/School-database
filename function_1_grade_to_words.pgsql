CREATE FUNCTION grade_to_words (grade float)
    RETURNS text
    AS $$
DECLARE
    result text;
BEGIN
    CASE TRUNC(grade)
    WHEN 6 THEN
        result = 'A';
    WHEN 5 THEN
        result = 'B';
    WHEN 4 THEN
        result = 'C';
    WHEN 3 THEN
        result = 'D';
    WHEN 2 THEN
        result = 'E';
    WHEN 1 THEN
        result = 'F';
    ELSE
        result = '';
    END CASE;
    IF grade - TRUNC(grade) = 0.5 THEN
        result = CONCAT(result, '+');
    END IF;
    RETURN result;
END;
$$
LANGUAGE plpgsql;

