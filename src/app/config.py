from utils.settings import Settings
from utils.singleton import Singleton
from .contextmanager import lifespan
from utils.settings import getSettings


class Settings(Settings, Singleton):
    app_name: str = getSettings().APP_NAME
    app_presets: dict = {
        'title': app_name,
        'lifespan': lifespan
    }
