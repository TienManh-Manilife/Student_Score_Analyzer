from webbrowser import get
from libs.database_lib.database import *
from libs.database_lib.evaluate_student_lib import *
from libs.draw.draw_chart import set_figure
import matplotlib.pyplot as plt

def get_x_y_of_linear_regression(MSSV):
    mlh = get_all_MLH_by_MSSV(MSSV)
    ma_lop_hoc = []
    time = []
    scores = []
    for MLH in mlh:
        get = get_time_of_a_Lophoc_by_MSSV(MLH, MSSV)
        if get is not None:
            time.append(get)
            ma_lop_hoc.append(MLH)
            scores.append(get_score_a_subject_by_MLH_of_a_student(MSSV, MLH))
    return np.array(time), np.array(scores)

def get_a_b_of_linear_regression(MSSV):
    time, scores = get_x_y_of_linear_regression(MSSV)
    return np.polyfit(time, scores, 1)

def draw_linear_regression(MSSV):
    time, scores = get_x_y_of_linear_regression(MSSV)
    a, b = get_a_b_of_linear_regression(MSSV)
    plt.figure(figsize=(15, 7))
    plt.plot(time, a * time + b, color='red', label=f'y = {a:.2f}x + {b:.2f}')
    plt.scatter(time, scores, color='blue')
    set_figure(plt.gcf(), f"Hồi quy tuyến tính dự đoán điểm số theo thời gian học của sinh viên {get_name_student(MSSV)} {MSSV}")
    plt.savefig(f"./resources/outputimages/draw_linear_regression_{MSSV}.png")
    plt.show()