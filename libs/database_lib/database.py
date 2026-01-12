import sqlite3

path = "./resources/database/students.db"
conn = sqlite3.connect(path)
cursor = conn.cursor()

def make_table_SinhVien():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS SinhVienn (
    MSSV INTEGER PRIMARY KEY,
    HoTen TEXT NOT NULL,
    NgaySinh DATE,
    MLH TEXT NOT NULL,
    FOREIGN KEY (MLH) REFERENCES LopHoc(MLH)
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
    FOREIGN KEY (MSSV) REFERENCES SinhVienn(MSSV),
    FOREIGN KEY (MLH, HocKy) REFERENCES LopHoc(MLH, HocKy)
    );
    """)

def insert_to_table_SinhVien(MSSV, HoTen, NgaySinh, MLH):
    cursor.execute("""
        INSERT INTO SinhVienn (MSSV, HoTen, NgaySinh, MLH) 
        VALUES (?, ?, ?, ?);
    """, (MSSV, HoTen, NgaySinh, MLH))
    conn.commit()

def insert_to_table_LopHoc(MLH, HocKy, Ten):
    cursor.execute("""
        INSERT INTO LopHoc (MLH, HocKy, Ten) 
        VALUES (?, ?, ?);
    """, (MLH, HocKy, Ten))
    conn.commit()

def insert_to_table_BangDiem(MLH, HocKy, MSSV, Diem):
    cursor.execute("""
        INSERT INTO BangDiem (MLH, HocKy, MSSV, Diem) 
        VALUES (?, ?, ?, ?);
    """, (MLH, HocKy, MSSV, Diem))
    conn.commit()


def make_all_tables():
    make_table_LopHoc()
    make_table_SinhVien()
    make_table_BangDiem()
    conn.commit()
    conn.close()