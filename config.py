import pydantic_settings
from dotenv import load_dotenv


class Config(pydantic_settings.BaseSettings):
    BASE_URL: str = 'https://github.com/'

load_dotenv()
config = Config()

