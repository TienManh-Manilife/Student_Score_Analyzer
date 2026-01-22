import sqlite3
from webbrowser import get
import pandas as pd
import numpy as np

path_students_db = "./resources/database/students.db"
path_students_xlsx = "./resources/database/students.xlsx"
path_classes_xlsx = "./resources/database/classes.xlsx"
path_scores_xlsx = "./resources/database/scores.xlsx"
path_time_xlsx = "./resources/database/time.xlsx"
conn = sqlite3.connect(path_students_db)
cursor = conn.cursor()
df_students = pd.read_excel(path_students_xlsx)
df_classes = pd.read_excel(path_classes_xlsx)
df_scores = pd.read_excel(path_scores_xlsx)
df_time = pd.read_excel(path_time_xlsx)

def make_table_SinhVien():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS SinhVien (
    MSSV INTEGER PRIMARY KEY,
    HoTen TEXT NOT NULL
    );
    """)

def make_table_LopHoc():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS LopHoc (
    MLH TEXT NOT NULL,
    HocKy INTEGER NOT NULL,
    Ten TEXT NOT NULL,
    PRIMARY KEY (MLH)
    );
    """)

def make_table_BangDiem():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS BangDiem (
    MLH TEXT NOT NULL,
    HocKy INTEGER NOT NULL,
    MSSV INTEGER NOT NULL,
    Diem REAL NOT NULL,
    PRIMARY KEY (MLH, MSSV),
    FOREIGN KEY (MSSV) REFERENCES SinhVien(MSSV),
    FOREIGN KEY (MLH) REFERENCES LopHoc(MLH)
    );
    """)

def make_table_ThoiGianHoc():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ThoiGianHoc (
    MSSV INTEGER NOT NULL,
    MLH TEXT NOT NULL,
    ThoiGianHoc REAL NOT NULL,
    PRIMARY KEY (MLH, MSSV),
    FOREIGN KEY (MSSV) REFERENCES SinhVien(MSSV),
    FOREIGN KEY (MLH) REFERENCES LopHoc(MLH)
    );
    """)


def insert_to_table_SinhVien(MSSV, HoTen):
    cursor.execute("""
        INSERT OR REPLACE INTO SinhVien (MSSV, HoTen) 
        VALUES (?, ?);
    """, (MSSV, HoTen))
    conn.commit()

def insert_to_table_LopHoc(MLH, HocKy, Ten):
    cursor.execute("""
        INSERT OR REPLACE INTO LopHoc (MLH, HocKy, Ten) 
        VALUES (?, ?, ?);
    """, (MLH, HocKy, Ten))
    conn.commit()

def insert_to_table_BangDiem(MLH, HocKy, MSSV, Diem):
    cursor.execute("""
        INSERT OR REPLACE INTO BangDiem (MLH, HocKy, MSSV, Diem) 
        VALUES (?, ?, ?, ?);
    """, (MLH, HocKy, MSSV, Diem))
    conn.commit()

def insert_to_table_ThoiGianHoc(MSSV, MLH, ThoiGianHoc):
    cursor.execute("""
        INSERT OR REPLACE INTO ThoiGianHoc (MSSV, MLH, ThoiGianHoc) 
        VALUES (?, ?, ?);
    """, (MSSV, MLH, ThoiGianHoc))
    conn.commit()

def insert_to_all_table():
    get_info_in_file_resources_database_students_xlsx()
    get_info_in_file_resources_database_classes_xlsx()
    get_info_in_file_resources_database_scores_xlsx()

def make_all_tables():
    make_table_LopHoc()
    make_table_SinhVien()
    make_table_BangDiem()
    make_table_ThoiGianHoc()
    conn.commit()

def get_info_in_file_resources_database_students_xlsx():
    for _, row in df_students.iterrows(): 
        MSSV = int(row.iloc[0]) 
        HoTen = str(row.iloc[1]) 
        insert_to_table_SinhVien(MSSV, HoTen)

def get_info_in_file_resources_database_time_xlsx():
    for _, row in df_time.iterrows(): 
        for i in range(0, 6):
            MLH = str(row.iloc[i*3 + 0]) 
            MSSV = int(row.iloc[i*3 + 1])
            ThoiGianHoc = str(row.iloc[i*3 + 2]) 
            insert_to_table_ThoiGianHoc(MSSV, MLH, ThoiGianHoc)

def print_all_SinhVien():
    cursor.execute("SELECT * FROM SinhVien;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def print_all_LopHoc():
    cursor.execute("SELECT * FROM LopHoc;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def get_info_in_file_resources_database_classes_xlsx():
    for _, row in df_classes.iterrows(): 
        MLH = str(row.iloc[0]) 
        HocKy = int(row.iloc[1])
        Ten = str(row.iloc[2]) 
        insert_to_table_LopHoc(MLH, HocKy, Ten)

def get_info_in_file_resources_database_scores_xlsx():
    for _, row in df_scores.iterrows(): 
        for i in range(0, 6):
            MLH = str(row.iloc[i*4 + 0]) 
            HocKy = int(row.iloc[i*4 + 1])
            MSSV = str(row.iloc[i*4 + 2]) 
            Diem = float(row.iloc[i*4 + 3])
            insert_to_table_BangDiem(MLH, HocKy, MSSV, Diem)

def print_all_BangDiem():
    cursor.execute("SELECT * FROM BangDiem;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def drop_all_table_in_database():
    cursor.execute("DROP TABLE BangDiem;")
    cursor.execute("DROP TABLE SinhVien;")
    cursor.execute("DROP TABLE LopHoc;")
    cursor.execute("DROP TABLE ThoiGianHoc;")

def get_all_score_in_a_LopHoc(MLH):
    cursor.execute("SELECT Diem FROM BangDiem Where MLH = ?", (MLH,))
    rows = cursor.fetchall()
    return [row[0] for row in rows]

def get_mean_all_score_in_a_LopHoc(MLH):
    cursor.execute("SELECT Diem FROM BangDiem Where MLH = ?", (MLH,))
    rows = cursor.fetchall()
    scores = [row[0] for row in rows]
    return round(np.mean(scores), 2)

def get_all_MLH():
    cursor.execute("SELECT MLH FROM LopHoc")
    rows = cursor.fetchall()
    return [row[0] for row in rows]

def get_all_MLH_by_MSSV(MSSV):
    cursor.execute("SELECT distinct MLH FROM BangDiem WHERE MSSV = ?", (MSSV,))
    rows = cursor.fetchall()
    return [row[0] for row in rows]

def get_name_LopHoc(MLH):
    cursor.execute("SELECT Ten FROM LopHoc WHERE MLH = ?", (MLH,))
    row = cursor.fetchone()
    return row[0]

def get_all_MLH_in_a_HocKy(HocKy):
    cursor.execute("SELECT MLH FROM LopHoc Where HocKy = ?;", (HocKy,))
    rows = cursor.fetchall()
    return [row[0] for row in rows]

def get_score_a_subject_by_MLH_of_a_student(MSSV, MLH):
    cursor.execute("SELECT Diem FROM BangDiem Where MSSV = ? AND MLH = ?;", (MSSV, MLH, ))
    row = cursor.fetchone()
    if row is None:
        return None
    return row[0]

def get_time_of_a_Lophoc_by_MSSV(MLH, MSSV):
    cursor.execute("SELECT ThoiGianHoc FROM ThoiGianHoc Where MSSV = ? AND MLH = ?;", (MSSV, MLH, ))
    row = cursor.fetchone()
    if row is None:
        return None
    return row[0]

def get_all_MLH_in_a_HocKy_of_a_student(MSSV, HocKy):
    cursor.execute("SELECT distinct BangDiem.MLH FROM LopHoc Join BangDiem ON LopHoc.MLH = BangDiem.MLH WHERE BangDiem.HocKy = ? AND BangDiem.MSSV = ?;", (HocKy, MSSV))
    rows = cursor.fetchall()
    return [row[0] for row in rows]

def change_HoTen_of_table_SinhVien(MSSV, HoTen_new):
    cursor.execute("""
        UPDATE SinhVien 
        SET HoTen = ?
        WHERE MSSV = ?;
    """, (HoTen_new, MSSV))
    conn.commit()

def change_Ten_of_table_LopHoc(MLH_old, Ten_new):
    cursor.execute("""
        UPDATE LopHoc 
        SET Ten = ?
        WHERE MLH = ?;
    """, (Ten_new, MLH_old))
    conn.commit()

def change_Diem_of_table_BangDiem(MLH_old, MSSV_old, Diem_new):
    cursor.execute("""
        UPDATE BangDiem 
        SET Diem = ?
        WHERE MLH = ? AND MSSV = ?;
    """, (Diem_new, MLH_old, MSSV_old))
    conn.commit()

def change_ThoiGianHoc_of_table_ThoiGianHoc(MSSV_old, MLH_old, ThoiGianHoc_new):
    cursor.execute("""
        UPDATE ThoiGianHoc 
        SET ThoiGianHoc = ?
        WHERE MSSV = ? AND MLH = ?;
    """, (ThoiGianHoc_new, MSSV_old, MLH_old))
    conn.commit()

def get_mean_time_a_HocKy_by_MSSV(MSSV, HocKy):
    cursor.execute("""
        SELECT ThoiGianHoc FROM ThoiGianHoc 
        JOIN LopHoc ON ThoiGianHoc.MLH = LopHoc.MLH
        WHERE ThoiGianHoc.MSSV = ? AND LopHoc.HocKy = ?;
    """, (MSSV, HocKy))
    rows = cursor.fetchall()
    times = [row[0] for row in rows]
    return round(np.mean(times), 2)