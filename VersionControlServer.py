from AccessControl import AccessController


class VersionControlServer:
    # region Vars
    # Access to db and sessions
    __session: AccessController

    # VersionControl





    # endregion
    # region Base
    def __init__(self):
        self.__session = AccessController("users.db", False)

    @property
    def session(self) -> AccessController:
        """
            Access to db and sessions
        """
        return self.__session

    # endregion
    # region VersionControl

    # endregion

