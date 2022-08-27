from dataclasses import dataclass
from main import Sepyre
from app.flet import *
import app


@dataclass()
class Settings(app.types.Page):
    main: Sepyre

    def __post_init__(self):
        pass

    def show(self):
        self.main.layout.show(Text('Settings Page'), f'Settings', 1)
        self.main.page.update()
