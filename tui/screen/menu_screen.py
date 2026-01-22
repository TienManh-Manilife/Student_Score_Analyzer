from textual.app import *
from textual.widgets import *
from tui.screen.base_screen import BaseScreen


class MenuScreen(BaseScreen):
    title = "MENU"
    is_menu = True

    def compose_content(self) -> ComposeResult:
        yield Button("Quay lại", id="back_button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id