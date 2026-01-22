from ast import In
from textual.app import *
from textual.widgets import *
from tui.screen.base_screen import BaseScreen

class DrawChartScreen(BaseScreen):
    title = "Vẽ biểu đồ"
    is_menu = False

    def compose_content(self) -> ComposeResult:
        yield Static("Vẽ biểu đồ thể hiện GPA của sinh viên qua các học kỳ")
        yield Input(placeholder="Nhập MSSV", id="mssv_input1")
        yield Button("Vẽ", id="draw_chart_each_gpa_of_a_student")

        yield Static("")
        
        yield Static("Vẽ biểu đồ thống kê GPA của tất cả sinh viên trong 1 học kỳ")
        yield Input(placeholder="Nhập học kỳ", id="hoc_ky_input2")
        yield Button("Vẽ", id="draw_chart_gpa_of_all_students_each_HocKy")

        yield Static("")

        yield Static("Vẽ biểu đồ thống kê CPA của tất cả sinh viên")
        yield Button("Vẽ", id="draw_chart_cpa_of_all_students")

        yield Static("")

        yield Static("Vẽ biểu đồ thống kê điểm trung bình tất cả sinh viên trong 1 lớp học")
        yield Input(placeholder="Nhập mã lớp học", id="ma_lop_hoc_input4")
        yield Button("Vẽ", id="draw_chart_scores_all_students_in_a_LopHoc")

        yield Static("")

        yield Static("Vẽ biểu đồ thống kê điểm tất cả môn học của 1 sinh viên trong 1 học kỳ")
        yield Input(placeholder="Nhập MSSV", id="mssv_input5")
        yield Input(placeholder="Nhập học kỳ", id="hoc_ky_input5")
        yield Button("Vẽ", id="draw_chart_scores_all_subjects_of_a_student_in_a_HocKy")

        yield Static("")

        yield Static("Vẽ biểu đồ thống kê điểm tất cả môn học của 1 sinh viên qua tất cả học kỳ")
        yield Input(placeholder="Nhập MSSV", id="mssv_input6")
        yield Button("Vẽ", id="draw_chart_scores_all_subjects_of_a_student_in_all_HocKy")

        yield Static("")

        yield Static("Vẽ biểu đồ thống kê điểm tất cả lớp học")
        yield Button("Vẽ", id="draw_chart_scores_all_classes")

        yield Static("")

        yield Static("Hồi quy tuyến tính dự đoán điểm số theo thời gian học của sinh viên")
        yield Input(placeholder="Nhập MSSV", id="mssv_input_linear_regression")
        yield Button("Vẽ", id="draw_chart_linear_regression")

        yield Static("")

        yield Static("Phân cụm K-Means điểm trung bình theo thời gian học của sinh viên")
        yield Input(placeholder="Nhập số cụm", id="num_clusters_input_k_means")
        yield Button("Vẽ", id="draw_chart_k_means")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        super().on_button_pressed(event)

    def on_key(self, event): 
        super().on_key(event)