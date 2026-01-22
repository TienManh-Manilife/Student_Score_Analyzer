from webbrowser import get
from textual.app import *
from textual.widgets import *
from libs.database_lib.database import get_name_LopHoc, get_score_a_subject_by_MLH_of_a_student
from libs.database_lib.evaluate_student_lib import get_all_MSSV, get_name_student
from tui.screen.base_screen import BaseScreen

class AClassScreen(BaseScreen):
    title = "Thao tác trong 1 lớp học"
    is_menu = False

    def compose_content(self) -> ComposeResult:
        yield Input(placeholder="Nhập mã lớp học", id="mlh_input_1")
        yield Button("Hiện tên lớp học", id="get_name_LopHoc_button")
        yield Static("", id="output1")
        yield Static("")
        yield Static("")
        yield Input(placeholder="Nhập mã lớp học", id="mlh_input_2")
        yield Button("Hiện điểm trung bình các sinh viên trong 1 lớp, điền mã lớp học vào bên trên", 
                     id="get_mean_all_score_in_a_LopHoc_button")
        yield Static("", id="output2")
        yield Static("")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        output_widget1 = self.query_one("#output1", Static)
        output_widget2 = self.query_one("#output2", Static)
        super().on_button_pressed(event)
        output = ""
        if button_id == "get_name_LopHoc_button":
            mlh = self.query_one("#mlh_input_1", Input).value
            mlh = str(mlh)
            try:
                output = get_name_LopHoc(mlh)
            except Exception as e:
                output = f"Chê! Không có lớp học này bạn nhé!"
            output_widget1.update(output)
            if output == "":
                output_widget1.update("Chưa có dữ liệu lớp học trong CSDL!")
            output = ""

        elif button_id == "get_mean_all_score_in_a_LopHoc_button":
            mlh = self.query_one("#mlh_input_2", Input).value
            try:
                output = f"Điểm trung bình của các sinh viên trong lớp {mlh} - {get_name_LopHoc(mlh)}:\n"
                MSSV = get_all_MSSV()
                for mssv in MSSV:
                    score = get_score_a_subject_by_MLH_of_a_student(mssv, mlh)
                    if score is not None:
                        output += f"{mssv} - {get_name_student(mssv)} - {score}\n"
                output_widget2.update(output)
                if output == "":
                    output_widget2.update("Chưa có dữ liệu lớp học trong CSDL!")
                output = ""
            except Exception as e:
                output = f"Chê! Không có lớp học này bạn nhé!"
                output_widget2.update(output)

    def on_key(self, event): 
        super().on_key(event)