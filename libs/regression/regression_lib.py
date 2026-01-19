from webbrowser import get
from libs.database_lib.database import *
from libs.database_lib.evaluate_student_lib import *
from libs.draw.draw_chart import set_figure
import matplotlib.pyplot as plt

def p():
    mssv = 24020220
    mlh = get_all_MLH_by_MSSV(mssv)
    ma_lop_hoc = []
    time = []
    scores = []
    for MLH in mlh:
        get = get_time_of_a_Lophoc_by_MSSV(MLH, mssv)
        if get is not None:
            time.append(get)
            ma_lop_hoc.append(MLH)
            scores.append(get_score_a_subject_by_MLH_of_a_student(mssv, MLH))
    return time, scores

def draw():
    time, scores = p()
    plt.scatter(time, scores, color='blue')
    set_figure(plt.gcf(), "Time")
    plt.show()