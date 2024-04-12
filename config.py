import dotenv
import pydantic_settings


class Config(pydantic_settings.BaseSettings):
    BASE_URL: str = 'https://github.com/'
    TIMEOUT: float = 4.5


dotenv.load_dotenv()
config = Config()
