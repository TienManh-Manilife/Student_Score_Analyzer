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

def change_score_to_4_and_word(score):
    if score >= 9.0:
        return 4, "A+"
    elif score >= 8.5:
        return 3.7, "A"
    elif score >= 8.0:
        return 3.5, "B+"
    elif score >= 7.0:
        return 3.0, "B"
    elif score >= 6.5:
        return 2.5, "C+"
    elif score >= 5.5:
        return 2.0, "C"
    elif score >= 5.0:
        return 1.5, "D+"
    elif score >= 4.0:
        return 1.0, "D"
    else:
        return 0, "F"
    
