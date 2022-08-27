from dataclasses import dataclass
from typing import Any
from main import Sepyre


@dataclass()
class Page():
    main: Sepyre

    def show(self):
        pass
