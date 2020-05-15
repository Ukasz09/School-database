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

# output
STUDENTS_CSV = "csv/students.csv"
TEACHERS_CSV = "csv/teachers.csv"
CLASSES_CSV = "csv/classes.csv"
MARKS_CSV = "csv/grades.csv"
TEACHING_CSV = "csv/teaching.csv"

csv_delimiter = ","
class_prefixes = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]
class_sufixes = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]
min_hourly_rate = 17
teacher_max_hourly_rate = 35
max_weekly_pensum = 40
general_class_profile = "ogolnoksztalcacy"
class_profiles = ["matematyczno-fizyczny", "humanistyczny", "matematyczno-geografizcny",
                  "informatyczny", "matematyczny", "biologiczny", "chamiczny", "biologiczno-chemiczny", "sportowy",
                  "artystyczny", "muzyczny"]
marks = [1, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5]


# -------------------------------------------------------------------------------------------------------------------- #
def csv_data_to_list(csv_filepath, data_from_columns=1, delim=",", quote='"'):
    with open(csv_filepath, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=delim, quotechar=quote)
        result = []
        for row in reader:
            result.append(row[data_from_columns])
    return result


def get_csv_file_to_write(csv_filepath, delim=","):
    csv_file = open(csv_filepath, 'w', newline='')
    return csv_file


def get_random_object(obj_list):
    index = random.randint(0, len(obj_list) - 1)
    return obj_list[index]


def get_random_object_with_removing(obj_list):
    index = random.randint(0, len(obj_list) - 1)
    obj = obj_list[index]
    del obj_list[index]
    return obj


def get_random_date(start, end):
    delta = end - start
    random_days = random.randrange(delta.days)
    return start + timedelta(days=random_days)


def format_date(date):
    return datetime.strftime(date, "%d-%m-%Y")


def get_random_class_symbol():
    return get_random_object(class_prefixes) + get_random_object(class_sufixes)


def get_random_profile(prop_for_general_profile):
    rand_numb = random.randint(0, 100)
    if rand_numb <= 100 * prop_for_general_profile:
        return general_class_profile
    else:
        return get_random_object(class_profiles)


# -------------------------------------------------------------------------------------------------------------------- #
female_names = csv_data_to_list(FEMALE_NAME_CSV)
male_names = csv_data_to_list(MALE_NAME_CSV)
surnames = csv_data_to_list(SURNAMES_CSV)
cities = csv_data_to_list(CITIES_CSV)


def generate_student_data(amount):
    csv_file = get_csv_file_to_write(STUDENTS_CSV)
    csv_writer = csv.writer(csv_file, delimiter=csv_delimiter)
    start_date = datetime.strptime("01-01-1990", "%d-%m-%Y")
    end_date = datetime.now() - timedelta(days=18 * 365)
    indexes = []
    for i in range(amount):
        sex = 'W' if random.randint(0, 1) == 0 else 'M'
        name = get_random_object(female_names) if sex == "W" else get_random_object(male_names)
        surname = get_random_object(surnames)
        birth_date = format_date(get_random_date(start_date, end_date))
        location = get_random_object(cities)
        class_symbol = get_random_class_symbol()
        csv_writer.writerow([i, surname, name, birth_date, sex, class_symbol, location])
        indexes.append(i)
    csv_file.close()
    return indexes


def generate_teacher_data(amount):
    csv_file = get_csv_file_to_write(TEACHERS_CSV)
    csv_writer = csv.writer(csv_file, delimiter=csv_delimiter)
    birth_start_date = datetime.strptime("01-01-1960", "%d-%m-%Y")
    birth_end_date = datetime.now() - timedelta(days=20 * 365)
    employment_end_date = datetime.now() - timedelta(days=2 * 365)
    indexes = []
    for i in range(amount):
        sex = 'W' if random.randint(0, 1) == 0 else 'M'
        name = get_random_object(female_names) if sex == "W" else get_random_object(male_names)
        surname = get_random_object(surnames)
        birth_date = get_random_date(birth_start_date, birth_end_date)
        employment_date = format_date(get_random_date(birth_date + timedelta(days=18 * 365), employment_end_date))
        hourly_rate = round(random.uniform(min_hourly_rate, teacher_max_hourly_rate), 2)
        pensum = random.randint(0, max_weekly_pensum)
        csv_writer.writerow([i, surname, name, employment_date, format_date(birth_date), sex, hourly_rate, pensum])
        indexes.append(i)
    csv_file.close()
    return indexes


def generate_school_classes(teachers_id_list, probability_of_general_profile):
    csv_file = get_csv_file_to_write(CLASSES_CSV)
    csv_writer = csv.writer(csv_file, delimiter=csv_delimiter)
    all_symbols = []
    # all possible classes
    for pref, suf in product(class_prefixes, class_sufixes):
        all_symbols.append(pref + suf)
    for symbol in all_symbols:
        profile = get_random_profile(probability_of_general_profile)
        tutor_id = get_random_object(teachers_id_list)
        csv_writer.writerow([symbol, profile, tutor_id])
    csv_file.close()
    return all_symbols


def generate_marks(amount, subjects_symbols_list, teacher_id_list, students_id_list):
    csv_file = get_csv_file_to_write(MARKS_CSV)
    csv_writer = csv.writer(csv_file, delimiter=csv_delimiter)
    start_date = datetime.strptime("01-01-2019", "%d-%m-%Y")
    end_date = datetime.strptime("31-12-2019", "%d-%m-%Y")
    for i in range(amount):
        stud_id = get_random_object(students_id_list)
        subj_id = get_random_object(subjects_symbols_list)
        teach_id = get_random_object(teacher_id_list)
        mark = get_random_object(marks)
        date = format_date(get_random_date(start_date, end_date))
        csv_writer.writerow([stud_id, subj_id, teach_id, mark, date])
    csv_file.close()


def generate_teaching(amount, teacher_id_list, subject_id_list):
    csv_file = get_csv_file_to_write(TEACHING_CSV)
    csv_writer = csv.writer(csv_file, delimiter=csv_delimiter)
    teacher_with_avail_subj = {}
    for id in teacher_id_list:
        teacher_with_avail_subj[id] = subject_id_list.copy()
    for i in range(amount):
        teacher_id = get_random_object(teacher_id_list)
        subject_id = get_random_object_with_removing(teacher_with_avail_subj.get(teacher_id))
        hours_per_week = random.randint(1, 20)
        csv_writer.writerow([teacher_id, subject_id, hours_per_week])
    csv_file.close()


if __name__ == "__main__":
    subject_id_list = csv_data_to_list(SUBJECTS_CSV, data_from_columns=0)
    stud_id_list = generate_student_data(600)
    teacher_id_list = generate_teacher_data(50)
    class_symbols = generate_school_classes(teacher_id_list, 0.3)
    generate_marks(200, subject_id_list, teacher_id_list, stud_id_list)
    generate_teaching(150, teacher_id_list, subject_id_list)
