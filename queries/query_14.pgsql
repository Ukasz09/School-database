-- Amount of waman and man in each class --
SELECT
    class_number || class_label AS class_symbol,
    COUNT(sex = 'W') AS women,
    COUNT(sex = 'M') AS men
FROM
    classes
    LEFT JOIN students ON students.class_id = classes.class_id
GROUP BY
    classes.class_id
ORDER BY
    class_number,
    class_label
