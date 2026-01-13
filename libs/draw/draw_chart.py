from cProfile import label
import matplotlib.pyplot as plt
from libs.database_lib.evaluate_student_lib import *

def draw_chart_each_gpa_of_a_student(MSSV):
    plt_draw = plt
    plt_draw = set_figure(plt_draw, f"GPA của sinh viên {get_name_student(MSSV)} ({MSSV}) qua các kỳ")
    gpa_each_HocKy = [get_gpa_4(MSSV, 12425), get_gpa_4(MSSV, 22425), get_gpa_4(MSSV, 12526), get_gpa_4(MSSV, 22526)]
    plt_draw.plot([1, 2, 3, 4], gpa_each_HocKy, "r-^", label="GPA từng kỳ")
    plt_draw.legend()
    plt_draw.savefig(f"./resources/output_images/draw_chart_each_gpa_of_a_student_{MSSV}")
    plt_draw.show()

def set_figure(plt_draw, title):
    plt_draw.figure(figsize=(15, 7))
    plt_draw.title(title)
    manager = plt_draw.get_current_fig_manager()
    manager.set_window_title(title)
    manager.window.wm_geometry("+0+0")
    return plt_draw