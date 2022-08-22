from dataclasses import dataclass
from main import Sepyre
from app.pages.library import Main
from app.pages.songs import Songs
from app.pages.song import Song
from app.pages.playlists import Playlists
import app.flet


@dataclass()
class Page():
    main: Sepyre
    page: app.flet.Page

    def show(self):
        pass

    def showEdit(self):
        pass
