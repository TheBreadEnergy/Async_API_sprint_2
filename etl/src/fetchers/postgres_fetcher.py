from psycopg import Connection, ServerCursor

from src.config import APP_SETTINGS
from src.loaders.base_repository import BaseRepository


class PostgresSource(BaseRepository):
    def __init__(self, pg_connection: Connection):
        self._pg_connection = pg_connection

    def fetch_many(self, size: int = APP_SETTINGS.batch_size):
        with ServerCursor(self._pg_connection, "fetcher") as cursor:
            while items := cursor.fetchmany(size):
                yield items
