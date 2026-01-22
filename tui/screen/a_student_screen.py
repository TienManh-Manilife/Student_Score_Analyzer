from webbrowser import get
from textual.app import *
from textual.widgets import *
from libs.database_lib.database import get_all_MLH_by_MSSV, get_name_LopHoc, get_score_a_subject_by_MLH_of_a_student, get_time_of_a_Lophoc_by_MSSV
from libs.database_lib.evaluate_student_lib import get_all_MSSV, get_name_student
from tui.screen.base_screen import BaseScreen

class AStudentScreen(BaseScreen):
    title = "Thao tác trong 1 sinh viên"
    is_menu = False

    def compose_content(self) -> ComposeResult:
        yield Static("Hiện các lớp học mà sinh viên theo học, điểm từng môn và thời gian học\n")
        yield Input(placeholder="Nhập mã sinh viên", id="mssv_input")
        yield Button("Hiện thông tin từng lớp theo học", id="get_all_classes_by_mssv_button")
        yield Static("")
        yield Static("", id="output")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        super().on_button_pressed(event)
        output_widget = self.query_one("#output", Static)
        output = ""
        if button_id == "get_all_classes_by_mssv_button":
            mssv = int(self.query_one("#mssv_input", Input).value)
            try:
                output = f"Các lớp học mà sinh viên {mssv} - {get_name_student(mssv)} theo học:\n"
                MLH = get_all_MLH_by_MSSV(mssv)
            except:
                output_widget.update("Chê! Không có sinh viên nào trong danh sách có mã đó!")
                return
            for mlh in MLH:
                score = get_score_a_subject_by_MLH_of_a_student(mssv, mlh)
                class_name = get_name_LopHoc(mlh)
                output += f"{mlh} - {class_name}: Điểm = {score} - Thời gian học: {get_time_of_a_Lophoc_by_MSSV(mlh, mssv)} giờ\n"
            output_widget = self.query_one("#output", Static)
            output_widget.update(output)

    def on_key(self, event): 
        super().on_key(event)