from textual.app import *
from textual.widgets import *
from tui.screen.base_screen import BaseScreen
from tui.screen.database_screen import DatabaseScreen


class MenuScreen(BaseScreen):
    title = "MENU"
    is_menu = True

    def compose_content(self) -> ComposeResult:
        yield Static("HIỆN TẠI ĐANG Ở MENU!")
        yield Button("Thao tác trong CSDL", id="database_button")
        yield Button("Thao tác trong tất cả lớp học", id="all_classes_button") # get_all_MLH, get_all_MLH_in_a_HocKy
        yield Button("Thao tác trong 1 lớp học", id="a_class_button") # get_mean_all_score_in_a_LopHoc, get_name_LopHoc
        yield Button("Thao tác trong 1 sinh viên", id="a_student_button") # get_all_MLH_by_MSSV, get_score_a_subject_by_MLH_of_a_student, get_time_of_a_Lophoc_by_MSSV
        # get_cpa_10, get_arr_cpa_10, get_arr_cpa_4, get_cpa_4, get_name_student, get_gpa_10, get_arr_gpa_10, get_arr_gpa_4, get_gpa_4, get_info_sinhvien

        yield Button("Thao tác trong tất cả sinh viên", id="all_students_button") # get_all_MSSV
        yield Button("Quy đổi và đánh giá", id="conversion_and_evaluation_button") # change_score_to_4, change_score_to_word, evaluate_academic_perfomance, evaluate_student
        yield Button("Vẽ biểu đồ", id="draw_chart_button") # draw_chart_each_gpa_of_a_student, draw_chart_gpa_of_all_students_each_HocKy
        # draw_chart_cpa_of_all_students, draw_chart_scores_all_students_in_a_LopHoc, draw_chart_scores_all_subjects_of_a_student_in_a_HocKy,
        # draw_chart_scores_all_subjects_of_a_student_in_all_HocKy, draw_chart_scores_all_LopHoc, draw_linear_regression, draw_chart_k_means
        yield Button("Thay đổi dữ liệu", id="change_data_button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        super().on_button_pressed(event)
        if button_id == "database_button":
            self.app.push_screen("DatabaseScreen")
        elif button_id == "all_classes_button":
            self.app.push_screen("AllClassesScreen")
        elif button_id == "a_class_button":
            return
        elif button_id == "a_student_button":
            return
        elif button_id == "conversion_and_evaluation_button":
            return
        elif button_id == "draw_chart_button":
            return
        elif button_id == "change_data_button":
            return

    def on_key(self, event): 
        super().on_key(event)