from ast import In
from textual.app import *
from textual.widgets import *
from tui.screen.base_screen import BaseScreen
from libs.draw.draw_chart import *
from libs.regression.regression_lib import draw_linear_regression
from libs.clusters.k_means import draw_chart_k_means

class DrawChartScreen(BaseScreen):
    title = "Vẽ biểu đồ"
    is_menu = False

    def compose_content(self) -> ComposeResult:
        yield Static("Vẽ biểu đồ thể hiện GPA của sinh viên qua các học kỳ")
        yield Input(placeholder="Nhập MSSV", id="mssv_input1")
        yield Button("Vẽ", id="draw_chart_each_gpa_of_a_student")
        yield Static("", id="output1")

        yield Static("")
        yield Static("")
        
        yield Static("Vẽ biểu đồ thống kê GPA của tất cả sinh viên trong 1 học kỳ")
        yield Input(placeholder="Nhập học kỳ", id="hoc_ky_input2")
        yield Button("Vẽ", id="draw_chart_gpa_of_all_students_each_HocKy")
        yield Static("", id="output2")

        yield Static("")
        yield Static("")

        yield Static("Vẽ biểu đồ thống kê CPA của tất cả sinh viên")
        yield Button("Vẽ", id="draw_chart_cpa_of_all_students")
        yield Static("", id="output3")

        yield Static("")
        yield Static("")

        yield Static("Vẽ biểu đồ thống kê điểm trung bình tất cả sinh viên trong 1 lớp học")
        yield Input(placeholder="Nhập mã lớp học", id="ma_lop_hoc_input4")
        yield Button("Vẽ", id="draw_chart_scores_all_students_in_a_LopHoc")
        yield Static("", id="output4")

        yield Static("")
        yield Static("")

        yield Static("Vẽ biểu đồ thống kê điểm tất cả môn học của 1 sinh viên trong 1 học kỳ")
        yield Input(placeholder="Nhập MSSV", id="mssv_input5")
        yield Input(placeholder="Nhập học kỳ", id="hoc_ky_input5")
        yield Button("Vẽ", id="draw_chart_scores_all_subjects_of_a_student_in_a_HocKy")
        yield Static("", id="output5")

        yield Static("")
        yield Static("")

        yield Static("Vẽ biểu đồ thống kê điểm tất cả môn học của 1 sinh viên qua tất cả học kỳ")
        yield Input(placeholder="Nhập MSSV", id="mssv_input6")
        yield Button("Vẽ", id="draw_chart_scores_all_subjects_of_a_student_in_all_HocKy")
        yield Static("", id="output6")

        yield Static("")
        yield Static("")

        yield Static("Vẽ biểu đồ thống kê điểm tất cả lớp học")
        yield Button("Vẽ", id="draw_chart_scores_all_LopHoc")
        yield Static("", id="output7")

        yield Static("")
        yield Static("")

        yield Static("Hồi quy tuyến tính dự đoán điểm số theo thời gian học của sinh viên")
        yield Input(placeholder="Nhập MSSV", id="mssv_input_linear_regression")
        yield Button("Vẽ", id="draw_chart_linear_regression")
        yield Static("", id="output8")

        yield Static("")
        yield Static("")

        yield Static("Phân cụm K-Means điểm trung bình theo thời gian học của sinh viên")
        yield Input(placeholder="Nhập số cụm", id="num_clusters_input_k_means")
        yield Button("Vẽ", id="draw_chart_k_means")
        yield Static("", id="output9")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        super().on_button_pressed(event)
        stt = 0
        try:
            if button_id == "draw_chart_each_gpa_of_a_student":
                stt = 1
                mssv = int(self.query_one("#mssv_input1", Input).value)
                draw_chart_each_gpa_of_a_student(mssv)

            elif button_id == "draw_chart_gpa_of_all_students_each_HocKy":
                stt = 2
                hoc_ky = int(self.query_one("#hoc_ky_input2", Input).value)
                draw_chart_gpa_of_all_students_each_HocKy(hoc_ky)
                
            elif button_id == "draw_chart_cpa_of_all_students":
                stt = 3
                draw_chart_cpa_of_all_students()
                
            elif button_id == "draw_chart_scores_all_students_in_a_LopHoc":
                stt = 4
                ma_lop_hoc = str(self.query_one("#ma_lop_hoc_input4", Input).value)
                draw_chart_scores_all_students_in_a_LopHoc(ma_lop_hoc)
                
            elif button_id == "draw_chart_scores_all_subjects_of_a_student_in_a_HocKy":
                stt = 5
                mssv = int(self.query_one("#mssv_input5", Input).value)
                hoc_ky = int(self.query_one("#hoc_ky_input5", Input).value)
                draw_chart_scores_all_subjects_of_a_student_in_a_HocKy(mssv, hoc_ky)
                
            elif button_id == "draw_chart_scores_all_subjects_of_a_student_in_all_HocKy":
                stt = 6
                mssv = int(self.query_one("#mssv_input6", Input).value)
                draw_chart_scores_all_subjects_of_a_student_in_all_HocKy(mssv)
                
            elif button_id == "draw_chart_scores_all_LopHoc":
                stt = 7
                draw_chart_scores_all_LopHoc()
                
            elif button_id == "draw_chart_linear_regression":
                stt = 8
                mssv = int(self.query_one("#mssv_input_linear_regression", Input).value)
                draw_linear_regression(mssv)
                
            elif button_id == "draw_chart_k_means":
                stt = 9
                num_clusters = int(self.query_one("#num_clusters_input_k_means", Input).value)
                draw_chart_k_means(num_clusters)
                
        except Exception as e:
            output_widget = self.query_one(f"#output{stt}", Static)
            output_widget.update(f"Lỗi: {str(e)}")
        output_widget = self.query_one(f"#output{stt}", Static)
        output_widget.update("Đã vẽ biểu đồ.")
        stt = 0

    def on_key(self, event): 
        super().on_key(event)