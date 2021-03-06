from data_generator import *

if __name__ == "__main__":
    teacher_id_list = generate_teacher_data(CLASSES_QTY * 2)
    class_id_list = generate_school_classes(teacher_id_list, 0.3)
    subject_id_list = csv_data_to_list(SUBJECTS_CSV, data_columns=0)
    stud_id_list = generate_student_data(600, class_id_list)
    generate_marks(400, subject_id_list, teacher_id_list, stud_id_list)
    generate_teaching(300, teacher_id_list, subject_id_list)
