from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')
    AccesskeyID: str | None=None
    SecretAccessKey: str | None=None
    region_name: str | None=None