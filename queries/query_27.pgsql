-- Full information about students --
CREATE VIEW students_info AS
SELECT
    student_id,
    stud.surname,
    stud.name,
    stud.birth_date,
    stud.sex,
    class_number || class_label AS class_symbol,
    cities.name AS city_name
FROM
    students AS stud
    LEFT JOIN classes ON stud.class_id = classes.class_id
    LEFT JOIN cities ON stud.residence_location = cities.city_id
ORDER BY
    surname,
    stud.name,
    class_number
