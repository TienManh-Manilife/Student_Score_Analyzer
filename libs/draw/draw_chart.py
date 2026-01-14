from typing import Counter
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
    fig, axes = plt.subplots(2, 2, figsize=(16,7))
    ax1, ax2, ax3, ax4 = axes.flatten()

    all_mssv = get_all_MSSV()
    all_gpa_HocKy = [get_gpa_4(mssv, HocKy) for mssv in all_mssv]
    evaluate = ["Giỏi", "Khá", "Trung bình", "Kém"]
    all_count_academic_prefomance = Counter([evaluate_academic_perfomance(mssv, HocKy) for mssv in all_mssv])
    count_evaluate = [all_count_academic_prefomance[ev] for ev in evaluate]

    set_figure(fig, f"GPA của tất cả sinh viên trong kỳ {HocKy}")
    evaluation_text = get_evaluation_text(all_gpa_HocKy)
    fig.text(0.55, 0.2, evaluation_text)

    ax1.plot(all_mssv, all_gpa_HocKy, "r-^", label="Điểm - MSSV tương ứng")
    ax1.set_title("Chi tiết điểm số")
    ax1.axhline(np.mean(all_gpa_HocKy), color="green", linestyle="--", label="Trung bình")
    ax1.set_xlabel("MSSV")
    ax1.set_ylabel("GPA")
    ax1.legend()

    ax2.hist(all_gpa_HocKy)
    ax2.set_title("Chi tiết điểm số")
    ax2.set_xlabel("MSSV")
    ax2.set_ylabel("GPA")

    ax4.boxplot(all_gpa_HocKy)
    ax4.set_ylabel("GPA")
    ax4.text(0.5, -0.25, "Phân bố GPA", ha='center', va='center', transform=ax4.transAxes, fontsize=12)
    ax4.legend()

    ax3.bar(evaluate, count_evaluate, color="skyblue", edgecolor="black")
    ax3.set_xlabel("Học lực")
    ax3.set_ylabel("Số sinh viên")
    ax3.text(0.5, -0.25, "Số lượng sinh viên theo học lực", ha='center', va='center', transform=ax3.transAxes, fontsize=12)

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
                    f"Q1: {q1}\nQ2: {q2}\nKhoảng tứ phân vị: {round(np.abs(q1-q2), 2)}"