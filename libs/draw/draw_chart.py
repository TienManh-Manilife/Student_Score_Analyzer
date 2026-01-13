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
    HocKy = ["Học kỳ I", "Học kỳ II", "Học kỳ III", "Học kỳ IV"]
    cpa = get_cpa_4(MSSV)

    ax.plot(HocKy, gpa_each_HocKy, "b-", label="GPA từng kỳ")
    ax.axhline(cpa, color="red", linestyle="--", label=f"Trung bình: {cpa}")
    ax.set_xlabel("Học kỳ")
    ax.set_ylabel("GPA")
    for i, j in zip(HocKy, gpa_each_HocKy): 
        ax.annotate(str(round(j,2)), xy=(i, j), xytext=(0,5), textcoords="offset points", ha="center", fontsize=10, color="green")

    evaluation_text = f"{HocKy[0]}: {evaluate_academic_perfomance(MSSV, 12425)}\n" \
        f"{HocKy[1]}: {evaluate_academic_perfomance(MSSV, 22425)}\n"\
        f"{HocKy[2]}: {evaluate_academic_perfomance(MSSV, 12526)}\n"\
        f"{HocKy[3]}: {evaluate_academic_perfomance(MSSV, 22526)}\n"\

    fig.text(0.01, 0.86, evaluation_text)
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
