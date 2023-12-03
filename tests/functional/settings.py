from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class TestSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="", env_file=".env")
    es_host: str = Field(
        "http://elastic:9200", env="ELASTIC_HOST", alias="ELASTIC_HOST"
    )
    es_movie_index: str = Field("movies", env="ES_MOVIE_INDEX", alias="ES_MOVIE_INDEX")
    es_genre_index: str = Field("genres", env="ES_GENRE_INDEX", alias="ES_GENRE_INDEX")
    es_person_index: str = Field(
        "persons", env="ES_PERSON_INDEX", alias="ES_PERSON_INDEX"
    )
    redis_host: str = Field("localhost", env="REDIS_HOST", alias="REDIS_HOST")
    redis_port: int = Field("6379", env="REDIS_PORT", alias="REDIS_PORT")
    service_url: str = Field(
        "http://film-api:8000", env="SERVICE_URL", alias="SERVICE_URL"
    )


test_settings = TestSettings()
