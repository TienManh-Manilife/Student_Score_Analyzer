#
## Mục đích
## Dữ liệu
- Cơ sở dữ liệu:
    - Bảng Sinh viên:
        - Mã số sinh viên: Lấy chính xác từ danh sách K69I-IT4 của UET
        - Họ và tên: Lấy chính xác từ danh sách K69I-IT4 của UET
        - Khóa chính: Mã số sinh viên
    - Bảng Lớp học:
        - Mã lớp học: Lấy chính xác mã của học phần chương trình đào tạo
        - Học Kỳ: Có 4 kì (12425, 22425, 12526, 22526)
        - Tên lớp học: Lấy chính xác tên của học phần chương trình đào tạo
        - Khóa chính: Mã lớp học + Học kỳ
    - Bảng điểm lớp học:
        - Mã lớp học: Như trên
        - Học Kỳ: Như trên
        - Mã số sinh viên: Như trên
        - Điểm: Vì bảo mật thông tin nên điểm số của tất cả sinh viên lấy ngẫu nhiên theo thuật toán tự bản thân đặt ra, không phải điểm thật của sinh viên
        - Khóa chính: Mã lớp học + Học kỳ + Mã số sinh viên
## Chức năng cơ bản
#### Một số hàm cần thiết khi sử dụng
- Chú ý: Các hàm đã tự động truy cập database, người dùng không cần truy cập lại. Không có hàm nào in ra màn hình vì mục đích vẽ biểu đồ, nếu muốn đơn lẻ hiện ra màn hình thì thêm print.
1. get_cpa_10(MSSV) và get_cpa_4(MSSV): Lấy CPA hệ 10 và hệ 4 của 1 sinh viên
2. get_arr_cpa_10(MSSV) và get_arr_cpa_4(MSSV): Lấy danh sách điểm trung bình từng môn tất cả các kỳ của 1 sinh viên theo hệ 10 và hệ 4
3. get_name_student(MSSV): Lấy tên sinh viên 
4. get_gpa_10(MSSV, HocKy) và get_gpa_4(MSSV, HocKy): Lấy GPA hệ 10 và hệ 4 của 1 Học kỳ
5. get_arr_gpa_10(MSSV, HocKy) và get_arr_gpa_4(MSSV, HocKy): Lấy điểm trung bình từng môn hệ 10 và hệ 4 của 1 Học kỳ
6. get_info_sinhvien(MSSV): Trả về tất cả thông tin và bảng điểm của sinh viên
7. change_score_to_4(score) và change_score_to_word(score): Chuyển điểm thành hệ 4 và hệ chữ
8. evaluate_academic_perfomance(MSSV, HocKy=None): Đánh giá học lực, mặc định là đánh giá tất cả kỳ nếu không truyền HocKy
9. evaluate_student(MSSV, HocKy=None): Đánh giá tất cả thông tin của 1 sinh viên
10. get_all_MSSV(): Trả về danh sách tất cả MSSV
#### GPA của 1 sinh viên trong tất cả các kỳ  
- Hướng dẫn vẽ: Sử dụng hàm sau trong main:
    draw_chart_each_gpa_of_a_student(MSSV)  
![./resources/output_images/draw_chart_each_gpa_of_a_student_24020220.png](./resources/output_images/draw_chart_each_gpa_of_a_student_24020220.png)
#### GPA của cả lớp trong 1 kỳ  
- Hướng dẫn vẽ: Sử dụng hàm sau trong main:
    draw_chart_gpa_of_all_students_a_HocKy(HocKy)  
    - HocKy: Có các kỳ như sau: 1, 2, 3, 4  
![./resources/output_images/draw_chart_gpa_of_all_students_a_HocKy_1.png](./resources/output_images/draw_chart_gpa_of_all_students_a_HocKy_1.png)  
![./resources/output_images/draw_chart_gpa_of_all_students_a_HocKy_2.png](./resources/output_images/draw_chart_gpa_of_all_students_a_HocKy_2.png)  
![./resources/output_images/draw_chart_gpa_of_all_students_a_HocKy_3.png](./resources/output_images/draw_chart_gpa_of_all_students_a_HocKy_3.png)  
![./resources/output_images/draw_chart_gpa_of_all_students_a_HocKy_4.png](./resources/output_images/draw_chart_gpa_of_all_students_a_HocKy_4.png)  
#### CPA của cả lớp  
![./resources/output_images/draw_chart_cpa_of_all_students.png](./resources/output_images/draw_chart_cpa_of_all_students.png)  
#### Thống kê dữ liệu điểm của 1 môn học  
#### Thống kê điểm từng môn trong 1 kỳ của 1 sinh viên
#### Thống kê điểm tất cả các môn trong tất cả kì của sinh viên
#### Thống kê điểm trung bình của tất cả các môn học với nhau