from dataclasses import dataclass
from main import Sepyre
from app.flet import *
import app


@dataclass()
class Song():
    main: Sepyre

    def __post_init__(self):
        pass

    def show(self):
        self.main.page.add(
            Text('Song Route')
        )
