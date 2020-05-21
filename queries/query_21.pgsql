-- Delete students from archieve whose have less than 20 years old --
DELETE FROM students_archieve
WHERE DATE_PART('year', AGE(birth_date)) < 20
