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
        self.main.layout.show(
            page=1,
            name=f'Settings',
            body=[
                Text('Settings Page')
            ]
        )
        self.main.page.update()
