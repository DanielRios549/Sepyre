from dataclasses import dataclass
from main import Sepyre
from app.pages.Main import Main
from app.pages.Songs import Songs
from app.pages.Playlists import Playlists
import app.flet


@dataclass()
class Page():
    main: Sepyre
    page: app.flet.Page

    def show(self):
        pass

    def showEdit(self):
        pass
