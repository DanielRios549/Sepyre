from dataclasses import dataclass
from main import Sepyre
from app.flet import *
import app


@dataclass()
class Playlists():
    main: Sepyre

    def __post_init__(self):
        self.items: Text

    def show(self):
        self.items = Text("Comming Soon.")
        return self.items

    def showEdit(self):
        self.items = Text("Updated")
        self.main.page.update()

        return self.items
