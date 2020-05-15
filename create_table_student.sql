CREATE TABLE Students (
    student_id integer NOT NULL PRIMARY KEY,
    surname varchar(80),
    name varchar(80),
    dateOfBirth DATE,
    sex CHAR(1),
    class_symbol varchar(8),
    residence_location varchar(30)
);