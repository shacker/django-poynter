import base64
import os
from pathlib import Path

from goodconf import Field, GoodConf

# Make this the same as in main settings:
BASE_DIR = Path(__file__).resolve().parent.parent


class AppConfig(GoodConf):
    """Configuration for template site. Pulls environment variables from
    the running instance and stores them as Django settings for use in code."""

    ALLOWED_HOSTS: list[str] = Field(default=["*"])

    # Load local env vars
    model_config = {"default_files": ["poynter/config/local.yml", "poynter/config/local.json"]}

    ASYNC_DEFAULT: str = Field(
        default="background", description="Controls whether async_task calls run in fg or bg."
    )
    DEBUG: bool = Field(default=False, description="Toggle debugging.")
    ENVIRONMENT: str = Field(
        default="localhost", description="Environment where application is deployed."
    )

    SECRET_KEY: str = Field(
        initial=lambda: base64.b64encode(os.urandom(60)).decode(),
        description="Used for cryptographic signing. "
        "https://docs.djangoproject.com/en/2.0/ref/settings/#secret-key",
    )

    DATABASE_URL: str = Field(
        default="postgres://localhost:5432/apppack-template", description="Database connection."
    )

    LOG_LEVEL: str = Field(default="INFO", description="Log level for application")

config = AppConfig()


def manage_py():
    """Entrypoint for manage.py"""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "poynter.config.settings")
    config.django_manage()


def generate_config():
    """Entrypoint for dumping out sample config"""
    print(config.generate_json(LOCAL_DEV=True, DEBUG=True, LOG_LEVEL="DEBUG"))
