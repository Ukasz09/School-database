-- Import data to tables from csv files --
COPY cities
FROM
    'csv_schoolDB/places_usa.csv' DELIMITERS ',' CSV;

COPY teachers
FROM
    'csv_schoolDB/teachers.csv' DELIMITERS ',' CSV;

COPY classes
FROM
    'csv_schoolDB/classes.csv' DELIMITERS ',' CSV;

COPY students
FROM
    'csv_schoolDB/students.csv' DELIMITERS ',' CSV;

COPY subjects
FROM
    'csv_schoolDB/subjects.csv' DELIMITERS ',' CSV;

COPY grades
FROM
    'csv_schoolDB/grades.csv' DELIMITERS ',' CSV;

COPY teaching
FROM
    'csv_schoolDB/teaching.csv' DELIMITERS ',' CSV;

