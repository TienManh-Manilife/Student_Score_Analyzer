from textual.app import *
from textual.widgets import *
from tui.screen.base_screen import BaseScreen
from libs.database_lib.database import *

class ChangeDataScreen(BaseScreen):
    title = "Thay đổi dữ liệu"
    is_menu = False

    def compose_content(self) -> ComposeResult:
        yield Static("Sửa đổi Họ tên trong bảng SinhVien")
        yield Input(placeholder="Nhập mssv", id="mssvLopHoc1")
        yield Input(placeholder="Nhập họ tên mới", id="name_input1")
        yield Button("Cập nhật họ tên", id="update_name_button1")
        yield Static("", id="output1")
        yield Static("")
        yield Static("")
        yield Static("Sửa đổi Tên lớp học trong bảng LopHoc")
        yield Input(placeholder="Nhập mã lớp học", id="mlh_input2")
        yield Input(placeholder="Nhập tên mới", id="name_input")
        yield Button("Cập nhật tên lớp học", id="update_name_button2")
        yield Static("", id="output2")
        yield Static("")
        yield Static("")
        yield Static("Sửa đổi điểm trong bảng BangDiem")
        yield Input(placeholder="Nhập mssv", id="mssv_input3")
        yield Input(placeholder="Nhập mã lớp học", id="mlh_input3")
        yield Input(placeholder="Nhập điểm mới", id="name_input3")
        yield Button("Cập nhật điểm", id="update_score_button3")
        yield Static("", id="output3")
        yield Static("")
        yield Static("")
        yield Static("Sửa đổi thời gian học trong bảng ThoiGianHoc")
        yield Input(placeholder="Nhập mssv", id="mssv_input4")
        yield Input(placeholder="Nhập mã lớp học", id="mlh_input4")
        yield Input(placeholder="Nhập thời gian học mới", id="time_input4")
        yield Button("Cập nhật thời gian học", id="update_time_button4")
        yield Static("", id="output4")
        yield Static("")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        super().on_button_pressed(event)
        stt = 0
        try:
            if button_id == "update_name_button1":
                stt = 1
                mssv = int(self.query_one("#mssvLopHoc1", Input).value)
                new_name = str(self.query_one("#name_input1", Input).value)
                change_HoTen_of_table_SinhVien(mssv, new_name)

            elif button_id == "update_name_button2":
                stt = 2
                mlh = self.query_one("#mlh_input2", Input).value
                new_name = str(self.query_one("#name_input", Input).value)
                change_Ten_of_table_LopHoc(mlh, new_name)

            elif button_id == "update_score_button3":
                stt = 3
                mssv = int(self.query_one("#mssv_input3", Input).value)
                mlh = self.query_one("#mlh_input3", Input).value
                new_score = float(self.query_one("#name_input3", Input).value)
                change_Diem_of_table_BangDiem(mssv, mlh, new_score)

            elif button_id == "update_time_button4":
                stt = 4
                mssv = int(self.query_one("#mssv_input4", Input).value)
                mlh = self.query_one("#mlh_input4", Input).value
                new_time = float(self.query_one("#time_input4", Input).value)
                change_ThoiGianHoc_of_table_ThoiGianHoc(mssv, mlh, new_time)
        except:
            output_widget = self.query_one(f"#output{stt}", Static)
            output_widget.update("Chê! Có lỗi rồi! He He He!")
            return
        if stt != 0:
            output_widget = self.query_one(f"#output{stt}", Static)
            output_widget.update("Thành công!")

    def on_key(self, event): 
        super().on_key(event)