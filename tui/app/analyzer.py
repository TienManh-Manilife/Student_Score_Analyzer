from textual.app import *
from textual.widgets import *
from tui.screen.menu_screen import MenuScreen

class AnalyzerApp(App):
    title = "Ứng dụng Thống kê và Phân tích Điểm số Sinh viên"

    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane(self.title):
                yield Static("Chào mừng đến với Ứng dụng Thống kê và Phân tích Điểm số Sinh viên!")
                yield Static("Dự án cá nhân của Nguyễn Tiến Mạnh - manilife217@gmail.com")
                yield Button("Vào menu", id="menu_button")
                yield Static("'Esc' để thoát ứng dụng.")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "menu_button":
            self.app.push_screen(MenuScreen())

    def on_key(self, event): 
        if event.key in ("escape"):
            self.exit()