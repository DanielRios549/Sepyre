from dataclasses import dataclass
from main import Sepyre
from app.flet import *
import app


@dataclass()
class Songs():
    main: Sepyre
    page: app.flet.Page

    def __post_init__(self):
        self.items: Text

    def show(self):
        self.items = Text("This is Tab 123")
        return self.items

    def showEdit(self):
        self.items = Text("Updated")
        self.page.update()

        return self.items
