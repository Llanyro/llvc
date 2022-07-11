from sys import platform
from enum import Enum


class Platform(Enum):
    WINDOWS = 0
    UNIX = 1
    OSX = 2


def get_platform() -> Platform:
    p: Platform = Platform.UNIX
    if platform == "linux" or platform == "linux2":
        p = Platform.UNIX
    elif platform == "win32":
        p = Platform.WINDOWS
    elif platform == "darwin":
        p = Platform.OSX
    return p

