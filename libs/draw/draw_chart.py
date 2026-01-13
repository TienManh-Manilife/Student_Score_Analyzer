import matplotlib.pyplot as plt
from libs.database_lib.evaluate_student_lib import *

def draw_chart_each_gpa_of_a_student(MSSV):
    HocKy = ["Học kỳ I", "Học kỳ II", "Học kỳ III", "Học kỳ IV"]
    cpa = get_cpa_4(MSSV)
    gpa_each_HocKy = [
        get_gpa_4(MSSV, 12425),
        get_gpa_4(MSSV, 22425),
        get_gpa_4(MSSV, 12526),
        get_gpa_4(MSSV, 22526)
    ]

    fig, ax = plt.subplots(figsize=(15, 7))
    set_figure(fig, f"GPA của sinh viên {get_name_student(MSSV)} ({MSSV}) qua các kỳ")

    ax.plot(HocKy, gpa_each_HocKy, "b-", label="GPA từng kỳ")
    ax.axhline(cpa, color="red", linestyle="--", label=f"Trung bình: {cpa}")
    ax.set_xlabel("Học kỳ")
    ax.set_ylabel("GPA")
    for i, j in zip(HocKy, gpa_each_HocKy): 
        ax.annotate(str(round(j,2)), xy=(i, j), xytext=(0,5), textcoords="offset points", ha="center", fontsize=10, color="green")

    evaluation_text = ""
    for i, j in zip(range(0, 4), [12425, 22425, 12526, 22526]):
        evaluation_text += f"{HocKy[i]}: {evaluate_academic_perfomance(MSSV, j)}\n"

    fig.text(0.01, 0.86, evaluation_text)
    ax.legend()
    fig.savefig(f"./resources/output_images/draw_chart_each_gpa_of_a_student_{MSSV}.png")
    plt.show()

def draw_chart_gpa_of_all_students_a_HocKy(HocKy):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15,7), sharey=True)
    set_figure(fig, f"GPA của tất cả sinh viên trong kỳ {HocKy}")
    all_mssv = get_all_MSSV()
    all_gpa_HocKy = [get_gpa_4(mssv, HocKy) for mssv in all_mssv]

    evaluation_text = get_evaluation_text(all_gpa_HocKy)

    ax1.plot(all_mssv, all_gpa_HocKy, "r-^", label="Điểm - MSSV tương ứng")
    fig.text(0.55, 0.65, evaluation_text)
    ax1.set_xlabel("MSSV")
    ax1.set_ylabel("GPA")
    ax1.legend()

    ax2.boxplot(all_gpa_HocKy)
    ax2.set_title("Phân bố GPA")
    ax2.set_ylabel("GPA")

    fig.savefig(f"./resources/output_images/draw_chart_gpa_of_all_students_a_HocKy_{HocKy}.png")
    plt.show()

def set_figure(fig, title):
    fig.suptitle(title) 
    manager = plt.get_current_fig_manager()
    manager.set_window_title(title)
    manager.window.wm_geometry("+0+0") 
    return fig

def get_evaluation_text(arr):
      q1 = round(np.percentile(arr, 25), 2)
      q2 = round(np.percentile(arr, 75), 2)
      return f"Max: {np.max(arr)}\nMin: {np.min(arr)}\n"\
                    f"Trung bình: {round(np.mean(arr), 2)}\nTrung vị: {round(np.median(arr), 2)}\n"\
                    f"Phương sai: {round(np.var(arr), 2)}\nĐộ lệch chuẩn: {round(np.std(arr), 2)}\n"\
                    f"Q1: {q1}\nQ2: {q2}\nKhoảng tứ phân vị: {np.abs(q1-q2)}"