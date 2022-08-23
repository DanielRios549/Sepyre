from dataclasses import dataclass
from main import Sepyre
from app.pages.library import Main
from app.pages.songs import Songs
from app.pages.song import Song
from app.pages.playlists import Playlists
from app import flet


@dataclass()
class Page():
    main: Sepyre
    page: flet.Page

    def show(self):
        pass

    def showEdit(self):
        pass
