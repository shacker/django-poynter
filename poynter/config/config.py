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


config = AppConfig()


def manage_py():
    """Entrypoint for manage.py"""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "poynter.config.settings")
    config.django_manage()


def generate_config():
    """Entrypoint for dumping out sample config"""
    print(config.generate_json(LOCAL_DEV=True, DEBUG=True, LOG_LEVEL="DEBUG"))
