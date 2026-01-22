from textual.app import *
from textual.widgets import *
from tui.screen.base_screen import BaseScreen

class ChangeDataScreen(BaseScreen):
    title = "Thay đổi dữ liệu"
    is_menu = False

    def compose_content(self) -> ComposeResult:
        yield Static("Chuyển điểm hệ 10 về hệ 4:\n\t[9.00; 10] -> 4.00\n\t[8.50; 9.00) -> 3.70\n\t[8.00; 8.50) -> 3.50\n\t[7.00; 8.00) -> 3.00\n\t[6.50; 7.00) -> 2.50\n\t[5.50; 6.50) -> 2.00\n\t[5.00; 5.50) -> 1.50\n\t[4.00; 5.00) -> 1.00\n\t[0; 4.00) -> 0.00")
        yield Static("Chuyển điểm hệ 10 về hệ chữ:\n\t[9.00; 10] -> A+\n\t[8.50; 9.00) -> A\n\t[8.00; 8.50) -> B+\n\t[7.00; 8.00) -> B\n\t[6.50; 7.00) -> C+\n\t[5.50; 6.50) -> C\n\t[5.00; 5.50) -> D+\n\t[4.00; 5.00) -> D\n\t[0; 4.00) -> F")
        yield Static("Chuyển điểm hệ 4 về hệ đánh giá học lực:\n\t[3.60 - 4.00] -> Xuất sắc\n\t[3.20 - 3.60) -> Giỏi\n\t[2.50 - 3.20) -> Khá\n\t[2.00 - 2.50) -> Trung bình\n\t[0.00 - 2.00) -> Kém")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        super().on_button_pressed(event)

    def on_key(self, event): 
        super().on_key(event)