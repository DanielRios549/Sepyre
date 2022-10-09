from dataclasses import dataclass
from pathlib import Path
from typing import TypedDict
from main import Sepyre


@dataclass()
class Page():
    main: Sepyre

    def show(self):
        pass


class Options(TypedDict):
    path: str
    folder: Path
    file: str


class Menu(TypedDict):
    label: str
    route: str
    icon: str
    selected_icon: str
