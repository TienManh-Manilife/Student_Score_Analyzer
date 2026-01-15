from libs.database_lib.database import *
from libs.database_lib.evaluate_student_lib import *
from libs.draw.draw_chart import *

if __name__ == "__main__":
    # draw_chart_scores_all_students_in_a_LopHoc("FLF1107")
    print(get_all_score_in_a_LopHoc("FLF1107"))