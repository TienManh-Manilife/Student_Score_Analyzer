from libs.database_lib.database import *
from libs.database_lib.evaluate_student_lib import *

if __name__ == "__main__":
    # make_all_tables()
    # get_info_in_file_resources_database_students_xlsx()
    # print_all_SinhVien()
    # get_info_in_file_resources_database_classes_xlsx()
    # print_all_LopHoc()
    # get_info_in_file_resources_database_scores_xlsx()
    # print_all_BangDiem()
    # print_info_sinhvien(24020220)
    print(get_gpa_10(24020220, 12425), " ", get_cpa_10(24020220))