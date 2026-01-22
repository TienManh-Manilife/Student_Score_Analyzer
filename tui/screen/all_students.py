from webbrowser import get
from textual.app import *
from textual.widgets import *
from libs.database_lib.database import get_name_LopHoc, get_score_a_subject_by_MLH_of_a_student
from libs.database_lib.evaluate_student_lib import get_all_MSSV, get_name_student
from tui.screen.base_screen import BaseScreen

class AllStudentsScreen(BaseScreen):
    title = "Thao tác trong tất cả sinh viên"
    is_menu = False

    def compose_content(self) -> ComposeResult:
        yield Static("Hiện thông tin tất cả sinh viên, mặc định sắp xếp theo MSSV")
        yield Button("Hiện thông tin tất cả sinh viên", id="get_all_MSSV_button")
        yield Static("")
        yield Static("", id="output")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        super().on_button_pressed(event)
        if button_id == "get_all_MSSV_button":
            MSSV = get_all_MSSV()
            output = "Danh sách tất cả sinh viên:\n"
            for mssv in MSSV:
                output += f"{mssv} - {get_name_student(mssv)}\n"
            output_widget = self.query_one("#output", Static)
            output_widget.update(output)
            output = ""

    def on_key(self, event): 
        super().on_key(event)