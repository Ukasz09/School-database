-- Amount of students from each city --
SELECT
    cities.name AS city,
    COUNT(students.residence_location) AS number_of_students
FROM
    cities
    LEFT JOIN students ON students.residence_location = cities.city_id
GROUP BY
    cities.city_id
ORDER BY
    number_of_students DESC
