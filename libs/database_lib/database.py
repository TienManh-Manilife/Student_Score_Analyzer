import sqlite3
import pandas as pd
import numpy as np

path_students_db = "./resources/database/students.db"
path_students_xlsx = "./resources/database/students.xlsx"
path_classes_xlsx = "./resources/database/classes.xlsx"
path_scores_xlsx = "./resources/database/scores.xlsx"
conn = sqlite3.connect(path_students_db)
cursor = conn.cursor()
df_students = pd.read_excel(path_students_xlsx)
df_classes = pd.read_excel(path_classes_xlsx)
df_scores = pd.read_excel(path_scores_xlsx)

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
    PRIMARY KEY (MLH, HocKy)
    );
    """)

def make_table_BangDiem():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS BangDiem (
    MLH TEXT NOT NULL,
    HocKy INTEGER NOT NULL,
    MSSV INTEGER NOT NULL,
    Diem REAL NOT NULL,
    PRIMARY KEY (MLH, HocKy, MSSV),
    FOREIGN KEY (MSSV) REFERENCES SinhVien(MSSV),
    FOREIGN KEY (MLH, HocKy) REFERENCES LopHoc(MLH, HocKy)
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


def make_all_tables():
    make_table_LopHoc()
    make_table_SinhVien()
    make_table_BangDiem()
    conn.commit()

def get_info_in_file_resources_database_students_xlsx():
    for _, row in df_students.iterrows(): 
        MSSV = int(row.iloc[0]) 
        HoTen = str(row.iloc[1]) 
        insert_to_table_SinhVien(MSSV, HoTen)
    conn.close()

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