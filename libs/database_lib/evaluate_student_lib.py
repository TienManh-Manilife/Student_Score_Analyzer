from .database import *
import numpy as np

max_HocKy = 4

def get_cpa_10(MSSV):
    cursor.execute("""
        SELECT b.Diem
        FROM SinhVien s
        JOIN BangDiem b ON s.MSSV = b.MSSV
        WHERE s.MSSV = ?;
    """, (MSSV,))
    rows = cursor.fetchall()
    scores = [row[0] for row in rows]
    return round(np.mean(scores), 2)

def get_arr_cpa_10(MSSV):
    cursor.execute("""
        SELECT b.Diem
        FROM SinhVien s
        JOIN BangDiem b ON s.MSSV = b.MSSV
        WHERE s.MSSV = ?;
    """, (MSSV,))
    rows = cursor.fetchall()
    return [row[0] for row in rows]

def get_arr_cpa_4(MSSV):
    return [change_score_to_4(score) for score in get_arr_cpa_10(MSSV)]

def get_cpa_4(MSSV):
    return round(np.mean(get_arr_cpa_4(MSSV)), 2)

def get_name_student(MSSV):
    cursor.execute("""
        SELECT HoTen
        FROM SinhVien
        WHERE MSSV = ?;
    """, (MSSV,))
    row = cursor.fetchone()
    return row[0]

def get_gpa_10(MSSV, HocKy):
    cursor.execute("""
        SELECT b.Diem
        FROM SinhVien s
        JOIN BangDiem b ON s.MSSV = b.MSSV
        WHERE s.MSSV = ? AND b.HocKy = ?;
    """, (MSSV, HocKy))
    rows = cursor.fetchall()
    scores = [row[0] for row in rows]
    return round(np.mean(scores), 2)

def get_arr_gpa_10(MSSV, HocKy):
    cursor.execute("""
        SELECT b.Diem
        FROM SinhVien s
        JOIN BangDiem b ON s.MSSV = b.MSSV
        WHERE s.MSSV = ? AND b.HocKy = ?;
    """, (MSSV, HocKy))
    rows = cursor.fetchall()
    return [row[0] for row in rows]

def get_arr_gpa_4(MSSV, HocKy):
    return [change_score_to_4(score) for score in get_arr_gpa_10(MSSV, HocKy)]

def get_gpa_4(MSSV, HocKy):
    return round(np.mean(get_arr_gpa_4(MSSV, HocKy)), 2)

def get_info_sinhvien(MSSV):
    cursor.execute("""
        SELECT s.MSSV, s.HoTen, l.MLH, l.HocKy, l.Ten, b.Diem
        FROM SinhVien s
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
    
def change_score_to_word(score):
    if score >= 9.0:
        return "A+"
    elif score >= 8.5:
        return "A"
    elif score >= 8.0:
        return "B+"
    elif score >= 7.0:
        return "B"
    elif score >= 6.5:
        return "C+"
    elif score >= 5.5:
        return "C"
    elif score >= 5.0:
        return "D+"
    elif score >= 4.0:
        return "D"
    else:
        return "F"
    
def evaluate_academic_perfomance(MSSV, HocKy=None):
    if HocKy is None:
        score = get_cpa_4(MSSV)
    else:
        score = score = get_gpa_4(MSSV, HocKy)
    if score >= 3.6:
        return "Xuất sắc"
    elif score >= 3.2:
        return "Giỏi"
    elif score >= 2.5:
        return "Khá"
    elif score >= 2.0:
        return "Trung bình"
    else:
        return "Kém"
    
def evaluate_student(MSSV, HocKy=None):
    if HocKy is None:
        return f"Sinh viên {get_name_student(MSSV)}:\n"\
        f"Điểm trung bình tích lũy tất cả (Hệ 10): {get_cpa_10(MSSV)}.\n"\
        f"Điểm trung bình tích lũy tất cả (Hệ 4): {get_cpa_4(MSSV)}.\n" \
        f"Học lực: {evaluate_academic_perfomance(MSSV)}"
    else:
        return f"Sinh viên {get_name_student(MSSV)}:\n"\
        f"Điểm trung bình tích lũy trong kỳ {HocKy} (Hệ 10): {get_gpa_10(MSSV, HocKy)}.\n"\
        f"Điểm trung bình tích lũy trong kỳ {HocKy} (Hệ 4): {get_gpa_4(MSSV, HocKy)}.\n" \
        f"Học lực trong kỳ {HocKy}: {evaluate_academic_perfomance(MSSV, HocKy)}"
    
def get_all_MSSV():
    cursor.execute("SELECT MSSV FROM SinhVien;")
    rows = cursor.fetchall()
    return [row[0] for row in rows]

def get_all_score_in_a_LopHoc(MLH):
    cursor.execute("SELECT Diem FROM BangDiem Where MLH = ?", (MLH,))
    rows = cursor.fetchall()
    return [row[0] for row in rows]

def get_all_MLH():
    cursor.execute("SELECT MLH FROM LopHoc")
    rows = cursor.fetchall()
    return [row[0] for row in rows]

def get_name_LopHoc(MLH):
    cursor.execute("SELECT Ten FROM LopHoc WHERE MLH = ?", (MLH,))
    row = cursor.fetchone()
    return row[0]