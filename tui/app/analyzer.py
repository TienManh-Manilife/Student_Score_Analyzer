from textual.app import *
from textual.widgets import *
from tui.screen.a_class_screen import AClassScreen
from tui.screen.a_student_screen import AStudentScreen
from tui.screen.all_classes_screen import AllClassesScreen
from tui.screen.all_students import AllStudentsScreen
from tui.screen.database_screen import DatabaseScreen
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

    def on_mount(self):
        self.install_screen(
            MenuScreen(),
            name="MenuScreen"
        )
        self.install_screen(
            DatabaseScreen(),
            name="DatabaseScreen"
        )
        self.install_screen(
            AllClassesScreen(),
            name="AllClassesScreen"
        )
        self.install_screen(
            AClassScreen(),
            name="AClassScreen"
        )
        self.install_screen(
            AllStudentsScreen(),
            name="AllStudentsScreen"
        )
        self.install_screen(
            AStudentScreen(),
            name="AStudentScreen"
        )