from main import Sepyre
from app.pages.tabs.songs import Songs
from app.pages.tabs.playlists import Playlists
from app.pages.library import Main
from app.pages.song import Song
from app.pages.settings import Settings
from app import types


def get(main: Sepyre, route: str) -> types.Page:
    routes = {
        'main': Main(main),
        'song': Song(main),
        'settings': Settings(main)
    }

    return routes[route]
