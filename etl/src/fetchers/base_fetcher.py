import abc

from src.config import APP_SETTINGS


class BaseLoader(abc.ABC):
    """Абстрактный класс хранилища данных.

    Позволяет получать пакетами данные из выбранного источника хранения данных.
    Способ получения данных может варироваться от базы данных с которой мы работаем
    """

    @abc.abstractmethod
    def fetch_many(self, size: int = APP_SETTINGS.batch_size):
        pass
