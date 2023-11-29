from uuid import UUID

from pydantic import BaseModel
from src.models.genre import Genre
from src.models.person import Person


class UUIDMixin(BaseModel):
    id: UUID


class Film(UUIDMixin):
    title: str
    imdb_rating: float | None
    description: str | None = None
    genres: list[Genre] | None = []
    actors: list[Person] | None = []
    writers: list[Person] | None = []
    director: list[str] | None = []


class Films(BaseModel):
    title: str
    imdb_rating: float | None
    description: str | None = None
