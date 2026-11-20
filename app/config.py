from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name:str = 'SafeBank Simulator'
    enviroment:str ='Development'
    database_url: str = 'sqlite:///./safe_bank.db'

    secret_key:str
    acess_token_minutes:int = 15

    model_config = SettingsConfigDict(env_file='.env',
                                      env_file_encoding='utf-8',)

settings = Settings()


