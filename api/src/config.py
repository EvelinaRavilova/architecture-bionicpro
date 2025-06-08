from typing import Annotated
from pydantic_settings import BaseSettings, ForceDecode

class Settings(BaseSettings):
  REACT_APP_URL: str = ""
  KEYCLOAK_SERVER_URL: str = ""
  KEYCLOAK_REALM_NAME: str = ""
  KEYCLOAK_CLIENT_ID: str = ""
  KEYCLOAK_ROLES_TO_ALLOW: Annotated[list[str], ForceDecode] = []

settings = Settings()
