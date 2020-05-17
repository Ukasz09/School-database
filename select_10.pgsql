-- Cities in which don't live any students --
SELECT
    cities.name AS city
FROM
    cities
    LEFT JOIN students ON students.residence_location = cities.city_id
WHERE
    students.name IS NULL
ORDER BY
    cities.name
