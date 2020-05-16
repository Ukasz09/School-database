CREATE TABLE cities (
    city_id integer PRIMARY KEY,
    name varchar(30) NOT NULL
);

CREATE TABLE teachers (
    teacher_id integer PRIMARY KEY,
    surname varchar(50) NOT NULL,
    name varchar(50) NOT NULL,
    employment_date date NOT NULL DEFAULT NOW(),
    birth_date date NOT NULL,
    sex char(1),
    hourly_rate float NOT NULL DEFAULT 17,
    teching_load integer NOT NULL DEFAULT 40,
    phone_no varchar(10)
);

CREATE TABLE classes (
    class_symbol varchar(6) PRIMARY KEY,
    profile varchar(50) NOT NULL DEFAULT 'general education',
    tutor_id integer REFERENCES teachers (teacher_id)
);

CREATE TABLE students (
    student_id integer PRIMARY KEY,
    surname varchar(50) NOT NULL,
    name varchar(50) NOT NULL,
    birth_date date NOT NULL,
    sex char(1),
    class_symbol varchar(6) REFERENCES classes (class_symbol),
    residence_location integer REFERENCES cities (city_id)
);

CREATE TABLE subjects (
    subject_id integer PRIMARY KEY,
    name varchar(50) NOT NULL
);

CREATE TABLE grades (
    student_id integer REFERENCES students (student_id),
    subject_id integer REFERENCES subjects (subject_id),
    teacher_id integer REFERENCES teachers (teacher_id),
    grade float NOT NULL,
    insertion_date date DEFAULT NOW()
);

CREATE TABLE teaching (
    teacher_id integer REFERENCES teachers (teacher_id),
    subject_id integer REFERENCES subjects (subject_id),
    hours_per_week integer NOT NULL,
    PRIMARY KEY (teacher_id, subject_id)
);