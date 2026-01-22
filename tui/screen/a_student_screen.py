from webbrowser import get
from textual.app import *
from textual.widgets import *
from libs.database_lib.database import get_all_MLH_by_MSSV, get_all_MLH_in_a_HocKy, get_name_LopHoc, get_score_a_subject_by_MLH_of_a_student, get_time_of_a_Lophoc_by_MSSV
from libs.database_lib.evaluate_student_lib import change_score_to_word, get_cpa_10, get_cpa_4, get_gpa_10, get_gpa_4, get_info_sinhvien, get_name_student
from tui.screen.base_screen import BaseScreen

class AStudentScreen(BaseScreen):
    title = "Thao tác trong 1 sinh viên"
    is_menu = False

    def compose_content(self) -> ComposeResult:
        yield Static("Hiện CPA và các lớp học mà sinh viên theo học, điểm từng môn và thời gian học")
        yield Input(placeholder="Nhập mã sinh viên", id="mssv_input1")
        yield Button("Hiện thông tin từng lớp theo học", id="get_all_classes_by_mssv_button")
        yield Static("", id="output1")
        yield Static("")
        yield Static("")
        yield Static("Hiện GPA và danh sách các môn của 1 học kỳ của 1 sinh viên")
        yield Input(placeholder="Nhập mã sinh viên", id="mssv_input2")
        yield Input(placeholder="Nhập học kỳ: 1, 2, 3, 4, 5, 6, 7", id="hoc_ky_input")
        yield Button("Hiện thông tin trong 1 học kỳ", id="get_gpa_by_mssv_button")
        yield Static("", id="output2")
        yield Static("")
        yield Static("")
        yield Static("Hiện tất cả thông tin trong CSDL của sinh viên dưới dạng các bộ sau khi join")
        yield Input(placeholder="Nhập mã sinh viên", id="mssv_input3")
        yield Button("Hiện thông tin", id="get_info_button")
        yield Static("", id="output3")
        yield Static("")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        super().on_button_pressed(event)
        output_widget1 = self.query_one("#output1", Static)
        output_widget2 = self.query_one("#output2", Static)
        output_widget3 = self.query_one("#output3", Static)
        output = ""
        if button_id == "get_all_classes_by_mssv_button":
            try:
                mssv = int(self.query_one("#mssv_input1", Input).value)
                output = f"CPA của sinh viên {mssv} - {get_name_student(mssv)}:\n   Hệ 10: {get_cpa_10(mssv)}\n   Hệ 4: {get_cpa_4(mssv)}\n"
                output += f"Các lớp học theo học:\n"
                MLH = get_all_MLH_by_MSSV(mssv)
            except:
                output_widget1.update("Chê! Không có sinh viên nào trong danh sách có mã đó!")
                return
            for mlh in MLH:
                score = get_score_a_subject_by_MLH_of_a_student(mssv, mlh)
                class_name = get_name_LopHoc(mlh)
                output += f"{mlh} - {class_name}:\n\t\tHệ 10 ({score})\tHệ chữ: ({change_score_to_word(score)})\tThời gian học: ({get_time_of_a_Lophoc_by_MSSV(mlh, mssv)}) giờ\n"
            output_widget1.update(output)
            output = ""

        elif button_id == "get_gpa_by_mssv_button":
            try:
                mssv = int(self.query_one("#mssv_input2", Input).value)
                hk = int(self.query_one("#hoc_ky_input", Input).value)
                output = f"GPA kỳ {hk} của sinh viên {mssv} - {get_name_student(mssv)}:\n Hệ 10: {get_gpa_10(mssv, hk)} - Hệ 4: {get_gpa_4(mssv, hk)}\n"
                output += f"Các lớp học theo học trong học kỳ {hk}:\n"
                MLH = get_all_MLH_in_a_HocKy(hk)
                for mlh in MLH:
                    score = get_score_a_subject_by_MLH_of_a_student(mssv, mlh)
                    class_name = get_name_LopHoc(mlh)
                    output += f"{mlh} - {class_name}:\n\t\tHệ 10 ({score})\tHệ chữ: ({change_score_to_word(score)})\tThời gian học: ({get_time_of_a_Lophoc_by_MSSV(mlh, mssv)}) giờ\n"
            except:
                output_widget2.update("Chê! Không có sinh viên nào trong danh sách có mã đó!")
                return
            output_widget2.update(output)
            output = ""

        elif button_id == "get_info_button":
            try:
                output = "Tất cả thông tin sinh viên trong CSDL:\n"
                mssv = int(self.query_one("#mssv_input3", Input).value)
                list = get_info_sinhvien(mssv)
                for l in list:
                    output += str(l) + "\n"
            except:
                output_widget3.update("Chê! Không có sinh viên nào trong danh sách có mã đó!")
                return
            output_widget3.update(output)
            output = ""

    def on_key(self, event): 
        super().on_key(event)