import logging
from typing import Any, Dict, List, Optional, Union, Tuple
from pydantic import AnyHttpUrl, BaseSettings, SecretStr


class Settings(BaseSettings):
    title: str = "ITEM MASTER"
    debug: bool
    docs_url: str = '/docs'
    openapi_prefix: str = ''
    openapi_url: str = '/openapi.json'
    redoc_url: str = '/redoc'
    version: str = '1.0.0'

    mysql_host: str
    mysql_port: int
    mysql_db_name: str
    mysql_user: str
    mysql_password: str

    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    allowed_hosts: list[str] = ["*"]

    logging_level: int = logging.INFO
    loggers: Tuple[str, str] = ('uvicorn.asgi', 'uvicorn.access')

    secret_key: SecretStr
    api_prefix: str = "/api/v1"

    jwt_token_prefix: str = 'Token'

    class Config:
        env_file = '.env'
        validate_assignment = True


    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            'debug': self.debug,
            'docs_url': self.docs_url,
            'openapi_prefix': self.openapi_prefix,
            'openapi_url': self.openapi_url,
            'redoc_url': self.redoc_url,
            'title': self.title,
            'version': self.version,
        }


    @property
    def database_url(self) -> str:
        return 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
            self.mysql_user,
            self.mysql_password,
            self.mysql_host,
            self.mysql_port,
            self.mysql_db_name
        )


settings = Settings()