-- Students from classes I, II or III --
SELECT
    student_id AS id,
    name,
    surname,
    class_number || class_label AS class_symbol
FROM
    students AS s
    INNER JOIN classes AS c ON s.class_id = c.class_id
WHERE
    c.class_number SIMILAR TO '(I|II|III)'
ORDER BY
    c.class_number,
    c.class_label
