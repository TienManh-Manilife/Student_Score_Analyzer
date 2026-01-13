from .database import *
import numpy as np

def get_cpa_10(MSSV):
    cursor.execute("""
        SELECT b.Diem
        FROM SinhVienn s
        JOIN BangDiem b ON s.MSSV = b.MSSV
        WHERE s.MSSV = ?;
    """, (MSSV,))
    rows = cursor.fetchall()
    scores = [row[0] for row in rows]
    return round(np.mean(scores), 2)

def get_arr_cpa_10(MSSV):
    cursor.execute("""
        SELECT b.Diem
        FROM SinhVienn s
        JOIN BangDiem b ON s.MSSV = b.MSSV
        WHERE s.MSSV = ?;
    """, (MSSV,))
    rows = cursor.fetchall()
    return [row[0] for row in rows]

def get_name_student(MSSV):
    cursor.execute("""
        SELECT HoTen
        FROM SinhVienn
        WHERE MSSV = ?;
    """, (MSSV,))
    row = cursor.fetchone()
    return row[0]

def get_gpa_10(MSSV, HocKy):
    cursor.execute("""
        SELECT b.Diem
        FROM SinhVienn s
        JOIN BangDiem b ON s.MSSV = b.MSSV
        WHERE s.MSSV = ? AND b.HocKy = ?;
    """, (MSSV, HocKy))
    rows = cursor.fetchall()
    scores = [row[0] for row in rows]
    return round(np.mean(scores), 2)

def print_info_sinhvien(MSSV):
    cursor.execute("""
        SELECT s.MSSV, s.HoTen, l.MLH, l.HocKy, l.Ten, b.Diem
        FROM SinhVienn s
        JOIN BangDiem b ON s.MSSV = b.MSSV
        JOIN LopHoc l ON b.MLH = l.MLH AND b.HocKy = l.HocKy
        WHERE s.MSSV = ?;
    """, (MSSV,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def change_score_to_4(score):
    if score >= 9.0:
        return 4
    elif score >= 8.5:
        return 3.7
    elif score >= 8.0:
        return 3.5
    elif score >= 7.0:
        return 3.0
    elif score >= 6.5:
        return 2.5
    elif score >= 5.5:
        return 2.0
    elif score >= 5.0:
        return 1.5
    elif score >= 4.0:
        return 1.0
    else:
        return 0

def get_arr_cpa_4(MSSV):
    return [change_score_to_4(score) for score in get_arr_cpa_10(MSSV)]

def get_cpa_4(MSSV):
    return round(np.mean(get_arr_cpa_4(MSSV)), 2)
    
def evaluate_academic_perfomance(MSSV, HocKy=None):
    if HocKy is None:
        return f"Sinh viên {get_name_student(MSSV)}:\n"\
        f"Điểm trung bình tích lũy (Hệ 10): {get_cpa_10(MSSV)}.\n"\
        f"Điểm trung bình tích lũy (Hệ 4): {get_cpa_4(MSSV)}.\n"