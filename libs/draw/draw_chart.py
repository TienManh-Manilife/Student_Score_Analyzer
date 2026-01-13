import matplotlib.pyplot as plt
from libs.database_lib.evaluate_student_lib import *

def draw_chart_each_gpa_of_a_student(MSSV):
    fig, ax = plt.subplots(figsize=(15, 7))
    set_figure(fig, f"GPA của sinh viên {get_name_student(MSSV)} ({MSSV}) qua các kỳ")

    gpa_each_HocKy = [
        get_gpa_4(MSSV, 12425),
        get_gpa_4(MSSV, 22425),
        get_gpa_4(MSSV, 12526),
        get_gpa_4(MSSV, 22526)
    ]

    ax.plot([1, 2, 3, 4], gpa_each_HocKy, "r-^", label="GPA từng kỳ")
    ax.set_xlabel("Học kỳ")
    ax.set_ylabel("GPA")
    ax.legend()
    fig.savefig(f"./resources/output_images/draw_chart_each_gpa_of_a_student_{MSSV}.png")
    plt.show()

def draw_chart_gpa_of_all_students_a_HocKy(HocKy):
    fig, ax = plt.subplots(figsize=(15, 7))
    set_figure(fig, f"GPA của tất cả sinh viên trong kỳ {HocKy}")

    all_gpa_HocKy = [get_gpa_4(mssv, HocKy) for mssv in get_all_MSSV()]
    ax.plot(get_all_MSSV(), all_gpa_HocKy, "r-^", label="Điểm - MSSV tương ứng")
    ax.set_xlabel("MSSV")
    ax.set_ylabel("GPA")
    ax.legend()
    fig.savefig(f"./resources/output_images/draw_chart_gpa_of_all_students_a_HocKy_{HocKy}.png")
    plt.show()

def set_figure(fig, title):
    fig.suptitle(title) 
    manager = plt.get_current_fig_manager()
    manager.set_window_title(title)
    manager.window.wm_geometry("+0+0") 
    return fig
