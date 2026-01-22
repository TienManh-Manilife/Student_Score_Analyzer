from math import e
from textual.app import *
from textual.widgets import *
from textual.screen import Screen

class BaseScreen(Screen):
    title = "MẶC ĐỊNH"
    is_menu = False

    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane(str(self.title)):
                yield from self.compose_content()

                if not self.is_menu:
                    yield Button("Quay lại Menu", id="back_button")
                yield Static("'Esc' để thoát ứng dụng.")

    def compose_content(self) -> ComposeResult:
        yield Static("Tab mặc định. Hãy ghi đè phương thức compose_content.")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "back_button":
            self.app.pop_screen()

    def on_key(self, event): 
        if event.key in ("escape"):
            self.exit()

    def exit(self):
        self.running = False