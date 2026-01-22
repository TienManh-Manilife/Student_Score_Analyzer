from webbrowser import get
from libs.database_lib.database import *
from libs.database_lib.evaluate_student_lib import *
from libs.draw.draw_chart import set_figure
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

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

def get_R2(MSSV):
    time, scores = get_x_y_of_linear_regression(MSSV)
    a, b = get_a_b_of_linear_regression(MSSV)
    y_pred = a * time + b
    ss_res = np.sum((scores - y_pred)**2) 
    ss_tot = np.sum((scores - np.mean(scores))**2) 
    r2 = 1 - ss_res/ss_tot
    return round(r2, 2)

def get_rmse(mssv):
    x, y = get_x_y_of_linear_regression(mssv)
    a, b = get_a_b_of_linear_regression(mssv)
    y_pred = a*x + b
    return np.sqrt(mean_squared_error(y, y_pred))

def draw_linear_regression(MSSV):
    time, scores = get_x_y_of_linear_regression(MSSV)
    a, b = get_a_b_of_linear_regression(MSSV)
    plt.figure(figsize=(15, 7))
    plt.plot(time, a * time + b, color='red', label=f'y = {a:.2f}x + {b:.2f}')
    plt.scatter(time, scores, color='blue')
    plt.text(0.05, 0.95, f" Hệ số R² xấp xỉ: {get_R2(MSSV)}", transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
    plt.xlabel("Thời gian học")
    plt.ylabel("Điểm số")
    set_figure(plt.gcf(), f"Hồi quy tuyến tính dự đoán điểm số theo thời gian học của sinh viên {get_name_student(MSSV)} {MSSV}")
    plt.legend()
    plt.savefig(f"./resources/outputimages/draw_linear_regression_{MSSV}.png")
    plt.show()