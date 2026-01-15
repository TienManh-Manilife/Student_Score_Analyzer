from typing import Counter
import matplotlib.pyplot as plt
from libs.database_lib.database import get_all_MLH, get_all_MLH_in_a_HocKy, get_score_a_subject_by_MLH_of_a_student, get_mean_all_score_in_a_LopHoc
from libs.database_lib.evaluate_student_lib import change_score_to_word, get_all_MSSV, get_all_score_in_a_LopHoc, get_cpa_4, get_name_LopHoc, max_HocKy, get_gpa_4, get_name_student, evaluate_academic_perfomance
import numpy as np
import mplcursors

def draw_chart_each_gpa_of_a_student(MSSV):
    HocKy = [f"Học kỳ {HK}" for HK in range(1, max_HocKy+1)]
    cpa = get_cpa_4(MSSV)
    gpa_each_HocKy = [get_gpa_4(MSSV, HK) for HK in range(1, max_HocKy+1)]

    fig, ax = plt.subplots(figsize=(15, 7))
    set_figure(fig, f"GPA của sinh viên {get_name_student(MSSV)} ({MSSV}) qua các kỳ")

    ax.plot(HocKy, gpa_each_HocKy, "b-", label="GPA từng kỳ")
    ax.axhline(cpa, color="red", linestyle="--", label=f"Trung bình: {cpa}")
    ax.set_xlabel("Học kỳ")
    ax.set_ylabel("GPA")
    for i, j in zip(HocKy, gpa_each_HocKy): 
        ax.annotate(str(round(j,2)), xy=(i, j), xytext=(0,5), textcoords="offset points", ha="center", fontsize=10, color="green")

    evaluation_text = ""
    for i in range(0, max_HocKy):
        evaluation_text += f"{HocKy[i]}: {evaluate_academic_perfomance(MSSV, i)}\n"

    fig.text(0.01, 0.86, evaluation_text)
    ax.legend()
    fig.savefig(f"./resources/output_images/draw_chart_each_gpa_of_a_student_{MSSV}.png")
    plt.show()

def draw_chart_gpa_of_all_students_each_HocKy(HocKy):
    fig, axes = plt.subplots(2, 2, figsize=(16,7))
    ax1, ax2, ax3, ax4 = axes.flatten()

    all_mssv = get_all_MSSV()
    all_gpa_HocKy = [get_gpa_4(mssv, HocKy) for mssv in all_mssv]
    evaluate = ["Xuất sắc", "Giỏi", "Khá", "Trung bình", "Kém"]
    all_count_academic_prefomance = Counter([evaluate_academic_perfomance(mssv, HocKy) for mssv in all_mssv])
    count_evaluate = [all_count_academic_prefomance[ev] for ev in evaluate]

    set_figure(fig, f"GPA của tất cả sinh viên trong kỳ {HocKy}")
    evaluation_text = get_evaluation_text(all_gpa_HocKy)
    fig.text(0.55, 0.2, evaluation_text)

    ax1 = set_ax1_plot(ax1, all_mssv, all_gpa_HocKy, "Chi tiết điểm số", "Điểm - MSSV tương ứng", "MSSV", "GPA")
    ax2 = set_ax2_hist(ax2, all_gpa_HocKy, "Chi tiết điểm số", "MSSV", "GPA")
    ax3 = set_ax3_bar(ax3, evaluate, count_evaluate, "Học lực", "Số sinh viên", 
                      0.5, -0.25, "Số lượng sinh viên theo học lực")
    ax4 = set_ax4_boxplot(ax4, all_gpa_HocKy, "GPA", 0.5, -0.25, "Phân bố GPA")

    fig.savefig(f"./resources/output_images/draw_chart_gpa_of_all_students_each_HocKy_{HocKy}.png")
    plt.show()

def draw_chart_cpa_of_all_students():
    fig, axes = plt.subplots(2, 2, figsize=(16,7))
    ax1, ax2, ax3, ax4 = axes.flatten()
    set_figure(fig, "CPA của tất cả sinh viên")

    all_mssv = get_all_MSSV()
    all_gpa_HocKy = [get_cpa_4(mssv) for mssv in all_mssv]
    evaluate = ["Xuất sắc", "Giỏi", "Khá", "Trung bình", "Kém"]
    all_count_academic_prefomance = Counter([evaluate_academic_perfomance(mssv) for mssv in all_mssv])
    count_evaluate = [all_count_academic_prefomance[ev] for ev in evaluate]

    evaluation_text = get_evaluation_text(all_gpa_HocKy)
    fig.text(0.55, 0.2, evaluation_text)

    ax1 = set_ax1_plot(ax1, all_mssv, all_gpa_HocKy, "Chi tiết điểm số", "Điểm - MSSV tương ứng", "MSSV", "CPA")
    ax2 = set_ax2_hist(ax2, all_gpa_HocKy, "Chi tiết điểm số", "MSSV", "CPA")
    ax3 = set_ax3_bar(ax3, evaluate, count_evaluate, "Học lực", "Số sinh viên", 
                      0.5, -0.25, "Số lượng sinh viên theo học lực")
    ax4 = set_ax4_boxplot(ax4, all_gpa_HocKy, "GPA", 0.5, -0.25, "Phân bố GPA")

    fig.savefig(f"./resources/output_images/draw_chart_cpa_of_all_students.png")
    plt.show()

def draw_chart_scores_all_students_in_a_LopHoc(MLH):
    fig, axes = plt.subplots(2, 2, figsize=(16,7))
    ax1, ax2, ax3, ax4 = axes.flatten()
    set_figure(fig, f"Điểm {get_name_LopHoc(MLH)} của tất cả sinh viên")

    all_mssv = get_all_MSSV()
    all_scores_10 = get_all_score_in_a_LopHoc(MLH)
    all_scores_word = [change_score_to_word(ans) for ans in all_scores_10]
    evaluate = ["A+", "A", "B+", "B", "C+", "C", "D+", "D", "F"]
    all_count_academic_prefomance = Counter(all_scores_word)
    count_evaluate = [all_count_academic_prefomance[ev] for ev in evaluate]

    ax1 = set_ax1_plot(ax1, all_mssv, all_scores_10, "Chi tiết điểm số", "Điểm - MSSV tương ứng", "MSSV", "Điểm")
    ax2 = set_ax2_hist(ax2, all_scores_10, "Chi tiết điểm số", "MSSV", "Điểm")
    ax3 = set_ax3_bar(ax3, evaluate, count_evaluate, "Học lực", "Số sinh viên", 
                      0.5, -0.25, "Số lượng sinh viên theo học lực")
    ax4 = set_ax4_boxplot(ax4, all_scores_10, "GPA", 0.5, -0.25, "Phân bố điểm")
    fig.savefig(f"./resources/output_images/draw_chart_scores_all_students_in_a_LopHoc_{MLH}.png")
    plt.show()

def draw_chart_scores_all_subjects_of_a_student_in_a_HocKy(MSSV, HocKy):
    fig, axes = plt.subplots(2, 2, figsize=(16,7))
    ax1, ax2, ax3, ax4 = axes.flatten()
    set_figure(fig, f"Điểm các môn trong kỳ {HocKy} của sinh viên {get_name_student(MSSV)} {MSSV}")

    all_MLH = get_all_MLH_in_a_HocKy(HocKy)
    all_subjects = [get_name_LopHoc(mlh) for mlh in all_MLH]
    all_scores = [get_score_a_subject_by_MLH_of_a_student(MSSV, MLH) for MLH in all_MLH]
    all_scores_word = [change_score_to_word(ans) for ans in all_scores]
    evaluate = ["A+", "A", "B+", "B", "C+", "C", "D+", "D", "F"]
    all_count_academic_prefomance = Counter(all_scores_word)
    count_evaluate = [all_count_academic_prefomance[ev] for ev in evaluate]

    ax1 = set_ax1_plot(ax1, all_MLH, all_scores, "Điểm từng môn học", "Điểm - Môn tương ứng", "Môn học", "Điểm")
    ax2 = set_ax2_hist(ax2, all_scores, "Điểm từng môn học", "Môn học", "Điểm")
    ax3 = set_ax3_bar(ax3, evaluate, count_evaluate, "Học lực", "Số môn", 
                      0.5, -0.25, "Số lượng môn theo học lực")
    ax4 = set_ax4_boxplot(ax4, all_scores, "Điểm", 0.5, -0.25, "Phân bố điểm")

    evaluation_text = ""
    for i in range(0, len(all_subjects)):
        evaluation_text += f"{all_MLH[i]}: {all_subjects[i]} "
    fig.text(0.005, 0.93, evaluation_text)

    fig.savefig(f"./resources/output_images/draw_chart_scores_all_subjects_of_a_student_in_a_HocKy_{MSSV}_{HocKy}.png")
    plt.show()

def draw_chart_scores_all_subjects_of_a_student_in_all_HocKy(MSSV):
    fig, axes = plt.subplots(2, 2, figsize=(16,7))
    ax1, ax2, ax3, ax4 = axes.flatten()
    set_figure(fig, f"Điểm các môn trong tất cả các kỳ của sinh viên {get_name_student(MSSV)} {MSSV}")

    all_MLH = get_all_MLH()
    all_subjects = [get_name_LopHoc(mlh) for mlh in all_MLH]
    all_scores = [get_score_a_subject_by_MLH_of_a_student(MSSV, MLH) for MLH in all_MLH]
    all_scores_word = [change_score_to_word(ans) for ans in all_scores]
    evaluate = ["A+", "A", "B+", "B", "C+", "C", "D+", "D", "F"]
    all_count_academic_prefomance = Counter(all_scores_word)
    count_evaluate = [all_count_academic_prefomance[ev] for ev in evaluate]

    ax1 = set_ax1_plot(ax1, all_MLH, all_scores, "Điểm từng môn học", "Điểm - Môn tương ứng", "Môn học", "Điểm")
    ax2 = set_ax2_hist(ax2, all_scores, "Điểm từng môn học", "Môn học", "Điểm")
    ax3 = set_ax3_bar(ax3, evaluate, count_evaluate, "Học lực", "Số môn", 
                      0.5, -0.25, "Số lượng môn theo học lực")
    ax4 = set_ax4_boxplot(ax4, all_scores, "Điểm", 0.5, -0.25, "Phân bố điểm")

    evaluation_text = ""
    for i in range(0, len(all_subjects)):
        evaluation_text += f"{all_MLH[i]}: {all_subjects[i]}\n"
    fig.text(0.005, 0.15, evaluation_text, fontsize=6)

    fig.savefig(f"./resources/output_images/draw_chart_scores_all_subjects_of_a_student_in_all_HocKy_{MSSV}.png")
    plt.show()

def draw_chart_scores_all_LopHoc():
    fig, axes = plt.subplots(2, 2, figsize=(16,7))
    ax1, ax2, ax3, ax4 = axes.flatten()
    set_figure(fig, f"Điểm trung bình tất cả các lớp học")

    all_MLH = get_all_MLH()
    all_subjects = [get_name_LopHoc(mlh) for mlh in all_MLH]
    all_scores = [get_mean_all_score_in_a_LopHoc(MLH) for MLH in all_MLH]
    all_scores_word = [change_score_to_word(ans) for ans in all_scores]
    evaluate = ["A+", "A", "B+", "B", "C+", "C", "D+", "D", "F"]
    all_count_academic_prefomance = Counter(all_scores_word)
    count_evaluate = [all_count_academic_prefomance[ev] for ev in evaluate]

    ax1 = set_ax1_plot(ax1, all_MLH, all_scores, "Điểm từng môn học", "Điểm - Môn tương ứng", "Môn học", "Điểm")
    ax2 = set_ax2_hist(ax2, all_scores, "Điểm trung bình từng môn học", "Môn học", "Điểm")
    ax3 = set_ax3_bar(ax3, evaluate, count_evaluate, "Học lực trung bình", "Số môn", 
                      0.5, -0.25, "Số lượng môn theo học lực trung bình")
    ax4 = set_ax4_boxplot(ax4, all_scores, "Điểm", 0.5, -0.25, "Phân bố điểm")

    evaluation_text = ""
    for i in range(0, len(all_subjects)):
        evaluation_text += f"{all_MLH[i]}: {all_subjects[i]}\n"
    fig.text(0.005, 0.15, evaluation_text, fontsize=6)

    fig.savefig(f"./resources/output_images/draw_chart_scores_all_LopHoc.png")
    plt.show()

def set_ax1_plot(ax1, x, y, title, LABEL, xlabel, ylabel):
    ax1.plot(x, y, "r-^", label = LABEL)
    ax1.set_title(title)
    ax1.axhline(np.mean(y), color="green", linestyle="--", label="Trung bình")
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)
    scatter = ax1.scatter(x, y)
    cursor = mplcursors.cursor(scatter, hover=True)
    @cursor.connect("add")
    def on_add(sel): 
        sel.annotation.set_text(f"x={x[sel.index]}, y={y[sel.index]:.2f}")
    ax1.legend()
    return ax1

def set_ax2_hist(ax2, y, title, xlabel, ylabel):
    ax2.hist(y)
    ax2.set_title(title)
    ax2.set_xlabel(xlabel)
    ax2.set_ylabel(ylabel)
    return ax2

def set_ax3_bar(ax3, x, y, xlabel, ylabel, title_x, title_y, title):
    ax3.bar(x, y, color="skyblue", edgecolor="black")
    ax3.set_xlabel(xlabel)
    ax3.set_ylabel(ylabel)
    ax3.text(title_x, title_y, title, ha='center', va='center', transform=ax3.transAxes, fontsize=12)
    scatter = ax3.scatter(x, y)
    cursor = mplcursors.cursor(scatter, hover=True)
    @cursor.connect("add")
    def on_add(sel): 
        sel.annotation.set_text(f"x={x[sel.index]}, y={y[sel.index]:.2f}")
    return ax3

def set_ax4_boxplot(ax4, y, ylabel, title_x, title_y, xlabel):
    ax4.boxplot(y)
    ax4.set_ylabel(ylabel)
    ax4.text(title_x, title_y, xlabel, ha='center', va='center', transform=ax4.transAxes, fontsize=12)
    return ax4

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