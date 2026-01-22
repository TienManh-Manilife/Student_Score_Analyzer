from textual.app import *
from textual.widgets import *
from libs.database_lib.database import make_all_tables
from tui.screen.base_screen import BaseScreen


class MakeAllTablesScreen(BaseScreen):
    title = "Tạo tất cả bảng trong CSDL"
    is_menu = False

    def compose_content(self) -> ComposeResult:
        yield Button("Tạo tất cả bảng", id="make")
        yield Static("", id="message")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        super().on_button_pressed(event)
        if button_id == "make":
            make_all_tables()
            message_widget = self.query_one("#message", Static)
            message_widget.update("Đã tạo tất cả bảng trong CSDL!")
        

    def on_key(self, event): 
        super().on_key(event)