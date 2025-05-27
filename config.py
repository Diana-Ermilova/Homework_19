from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Config(BaseSettings):
    username: str
    accessKey: str
    app: str

config = Config()

