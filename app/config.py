from dataclasses import dataclass
from main import Sepyre


@dataclass()
class Config():
    main: Sepyre

    def __post_init__(self):
        self.separation = self.main.folder.joinpath('separation')
