import csv
import random
from datetime import datetime, timedelta
from itertools import product

# input
FEMALE_NAME_CSV = "csv/female_names.csv"
MALE_NAME_CSV = "csv/male_names.csv"
SURNAMES_CSV = "csv/surnames.csv"
CITIES_CSV = "csv/places_usa.csv"
SUBJECTS_CSV = "csv/subjects.csv"
CLASS_PROFILES_CSV = "csv/class_profiles.csv"

# output
STUDENTS_CSV = "csv/students.csv"
TEACHERS_CSV = "csv/teachers.csv"
CLASSES_CSV = "csv/classes.csv"
MARKS_CSV = "csv/grades.csv"
TEACHING_CSV = "csv/teaching.csv"

# others
CSV_DELIMITER = ","
CLASS_PREFIXES = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]
CLASS_SUFFIXES = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
GENERAL_CLASS_PROFILE = "general education"
GRADES = [1, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5]
MIN_HOURLY_RATE = 17
MAX_HOURLY_RATE = 35
MAX_WEEKLY_TEACHING_LOAD = 40


# -------------------------------------------------------------------------------------------------------------------- #
def csv_data_to_list(csv_filepath, data_columns=1, delimiter=",", quotechar='"'):
    with open(csv_filepath, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        return [row[data_columns] for row in reader]


def get_csv_write_file(csv_filepath):
    return open(csv_filepath, 'w', newline='')


def rand_elem(elem_list):
    index = random.randint(0, len(elem_list) - 1)
    return elem_list[index]


def remove_and_return_rand_elem(elem_list):
    index = random.randint(0, len(elem_list) - 1)
    obj = elem_list[index]
    del elem_list[index]
    return obj


def rand_date(start, end):
    delta = end - start
    random_days = random.randrange(delta.days)
    return start + timedelta(days=random_days)


def format_date(date):
    return datetime.strftime(date, "%d-%m-%Y")


def rand_class_symbol():
    return rand_elem(CLASS_PREFIXES) + rand_elem(CLASS_SUFFIXES)


def rand_profile(probability_of_general_profile):
    if random.randint(0, 100) <= 100 * probability_of_general_profile:
        return GENERAL_CLASS_PROFILE
    return rand_elem(csv_data_to_list(CLASS_PROFILES_CSV))


# -------------------------------------------------------------------------------------------------------------------- #
female_names = csv_data_to_list(FEMALE_NAME_CSV)
male_names = csv_data_to_list(MALE_NAME_CSV)
surnames = csv_data_to_list(SURNAMES_CSV)
cities = csv_data_to_list(CITIES_CSV)
all_possible_classes = [pref + suf for pref, suf in product(CLASS_PREFIXES, CLASS_SUFFIXES)]


def rand_student_birth_date():
    start_date = datetime.strptime("01-01-1990", "%d-%m-%Y")
    end_date = datetime.now() - timedelta(days=18 * 365)
    return rand_date(start_date, end_date)


def generate_student_data(amount):
    csv_file = get_csv_write_file(STUDENTS_CSV)
    csv_writer = csv.writer(csv_file, delimiter=CSV_DELIMITER)
    indexes = []
    for i in range(amount):
        sex = 'W' if random.randint(0, 1) == 0 else 'M'
        name = rand_elem(female_names) if sex == "W" else rand_elem(male_names)
        birth_date = format_date(rand_student_birth_date())
        csv_writer.writerow([i, rand_elem(surnames), name, birth_date, sex, rand_class_symbol(), rand_elem(cities)])
        indexes.append(i)
    csv_file.close()
    return indexes


def rand_teacher_birth_date():
    birth_start_date = datetime.strptime("01-01-1960", "%d-%m-%Y")
    birth_end_date = datetime.now() - timedelta(days=20 * 365)
    return rand_date(birth_start_date, birth_end_date)


def rand_teacher_employment_date(birth_date):
    employment_end_date = datetime.now() - timedelta(days=2 * 365)
    return rand_date(birth_date + timedelta(days=18 * 365), employment_end_date)


def generate_teacher_data(amount):
    csv_file = get_csv_write_file(TEACHERS_CSV)
    csv_writer = csv.writer(csv_file, delimiter=CSV_DELIMITER)
    indexes = []
    for i in range(amount):
        sex = 'W' if random.randint(0, 1) == 0 else 'M'
        name = rand_elem(female_names) if sex == "W" else rand_elem(male_names)
        birth_date = rand_teacher_birth_date()
        employment_date = format_date(rand_teacher_employment_date(birth_date))
        hourly_rate = round(random.uniform(MIN_HOURLY_RATE, MAX_HOURLY_RATE), 2)
        teaching_load = random.randint(0, MAX_WEEKLY_TEACHING_LOAD)
        row = [i, rand_elem(surnames), name, employment_date, format_date(birth_date), sex, hourly_rate, teaching_load]
        csv_writer.writerow(row)
        indexes.append(i)
    csv_file.close()
    return indexes


def generate_school_classes(teachers_id_list, probability_of_general_profile):
    csv_file = get_csv_write_file(CLASSES_CSV)
    csv_writer = csv.writer(csv_file, delimiter=CSV_DELIMITER)
    for symbol in all_possible_classes:
        profile = rand_profile(probability_of_general_profile)
        tutor_id = rand_elem(teachers_id_list)
        csv_writer.writerow([symbol, profile, tutor_id])
    csv_file.close()


def rand_grade_date():
    start_date = datetime.strptime("01-01-2019", "%d-%m-%Y")
    end_date = datetime.strptime("31-12-2019", "%d-%m-%Y")
    return rand_date(start_date, end_date)


def generate_marks(amount, subj_symb_list, teacher_id_list, stud_id_list):
    csv_file = get_csv_write_file(MARKS_CSV)
    csv_writer = csv.writer(csv_file, delimiter=CSV_DELIMITER)
    for i in range(amount):
        date = format_date(rand_grade_date())
        row = [rand_elem(stud_id_list), rand_elem(subj_symb_list), rand_elem(teacher_id_list), rand_elem(GRADES), date]
        csv_writer.writerow(row)
    csv_file.close()


def teacher_with_all_subjects_dict(subject_id_list):
    teacher_with_subjects = {}
    for teacher_id in teacher_id_list:
        teacher_with_subjects[teacher_id] = subject_id_list.copy()
    return teacher_with_subjects


def generate_teaching(amount, teacher_id_list, subject_id_list):
    csv_file = get_csv_write_file(TEACHING_CSV)
    csv_writer = csv.writer(csv_file, delimiter=CSV_DELIMITER)
    teacher_dict = teacher_with_all_subjects_dict(subject_id_list)
    for i in range(amount):
        teacher_id = rand_elem(teacher_id_list)
        subject_id = remove_and_return_rand_elem(teacher_dict.get(teacher_id))
        hours_per_week = random.randint(1, int(MAX_WEEKLY_TEACHING_LOAD / 3))
        csv_writer.writerow([teacher_id, subject_id, hours_per_week])
    csv_file.close()


if __name__ == "__main__":
    subject_id_list = csv_data_to_list(SUBJECTS_CSV, data_columns=0)
    stud_id_list = generate_student_data(600)
    teacher_id_list = generate_teacher_data(50)
    generate_school_classes(teacher_id_list, 0.3)
    generate_marks(200, subject_id_list, teacher_id_list, stud_id_list)
    generate_teaching(150, teacher_id_list, subject_id_list)
