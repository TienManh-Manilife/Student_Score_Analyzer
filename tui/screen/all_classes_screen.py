from textual.app import *
from textual.widgets import *
from tui.screen.base_screen import BaseScreen
from libs.database_lib.database import get_all_MLH, get_all_MLH_in_a_HocKy, get_name_LopHoc


class AllClassesScreen(BaseScreen):
    title = "Thao tác trong tất cả lớp học"
    is_menu = False

    def compose_content(self) -> ComposeResult:
        yield Button("Hiện tất cả mã lớp học", id="get_all_MLH_button")
        yield Static("")
        yield Static("")
        yield Input(placeholder="Nhập học kỳ là 1 số (1, 2, 3, 4, 5, 6, 7)", id="hoc_ky_input")
        yield Button("Hiện ra tất cả mã lớp học trong 1 học kỳ, điền học kỳ vào bên trên", id="get_all_MLH_in_a_HocKy_button")
        yield Static("")
        yield Static("")
        yield Static("THÔNG TIN ĐẦU RA:")
        yield Static("CHƯA CÓ!", id="output")
        yield Static("", id="message")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        output_widget = self.query_one("#output", Static)
        message_widget = self.query_one("#message", Static)
        super().on_button_pressed(event)
        output = ""
        if button_id == "get_all_MLH_button":
            MLH = get_all_MLH()
            output += "Tất cả danh sách mã lớp học:\n"
            for i in MLH:
                output += f"{str(i)}: {get_name_LopHoc(i)}\n"
            output_widget.update(output)
            if output == "":
                message_widget.update("Chưa có dữ liệu lớp học trong CSDL!")
        elif button_id == "get_all_MLH_in_a_HocKy_button":
            hk = self.query_one("#hoc_ky_input", Input).value
            hk = int(hk)
            if hk not in range(1, 8):
                output_widget.update("")
                message_widget.update("Học kỳ không hợp lệ! Vui lòng nhập học kỳ là 1 số từ 1 đến 7.")
                return
            output = f"Danh sách mã lớp học trong học kỳ {hk}:\n"
            MLH = get_all_MLH_in_a_HocKy(hk)
            for i in MLH:
                output += f"{str(i)}: {get_name_LopHoc(i)}\n"
            output_widget.update(output)
            if output == "":
                message_widget.update(f"Chưa có dữ liệu lớp học trong học kỳ {hk}!")

    def on_key(self, event): 
        super().on_key(event)