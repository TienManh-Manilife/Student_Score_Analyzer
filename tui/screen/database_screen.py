from textual.app import *
from textual.widgets import *
from libs.database_lib.database import drop_all_table_in_database, insert_to_all_table, make_all_tables
from tui.screen.base_screen import BaseScreen


class DatabaseScreen(BaseScreen):
    title = "Thao tác trong CSDL"
    is_menu = False

    def compose_content(self) -> ComposeResult:
        yield Button("Tạo tất cả bảng trong CSDL", id="make_all_tables_button")
        yield Button("Chèn dữ liệu từ xlsx vào tất cả bảng", id="insert_to_all_table_button")
        yield Button("Xóa tất cả bảng trong CSDL", id="drop_all_table_in_database_button")
        yield Static("", id="message")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        message_widget = self.query_one("#message", Static)
        super().on_button_pressed(event)
        if button_id == "make_all_tables_button":
            make_all_tables()
            message_widget.update("Đã tạo tất cả bảng trong CSDL!")
        elif button_id == "insert_to_all_table_button":
            message_widget.update("Đang chèn, vui lòng không ấn lung tung!")
            insert_to_all_table()
            message_widget.update("Đã chèn dữ liệu từ xlsx vào tất cả bảng!")
        elif button_id == "drop_all_table_in_database_button":
            drop_all_table_in_database()
            message_widget.update("Đã xóa tất cả bảng trong CSDL!")

    def on_key(self, event): 
        super().on_key(event)