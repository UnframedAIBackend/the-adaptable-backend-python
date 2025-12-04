import os
from pathlib import Path
from typing import Any, Dict

class Configuration:
    _instance = None
    _config: Dict[str, Any] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Configuration, cls).__new__(cls)
            cls._instance._load_env()
        return cls._instance

    def _load_env(self) -> None:
        env_path = Path(".env")
        if env_path.exists():
            with open(env_path) as f:
                for line in f:
                    if line.strip() and not line.startswith("#"):
                        try:
                            key, value = line.strip().split("=", 1)
                            os.environ[key] = value
                        except ValueError:
                            continue
        
        self._config["PORT"] = int(os.getenv("PORT", "3000"))
        self._config["NODE_ENV"] = os.getenv("NODE_ENV", "development")
        self._config["DATABASE_URL"] = os.getenv("DATABASE_URL")
        self._config["DATABASE_ENGINE"] = os.getenv("DATABASE_ENGINE")

    def get(self, key: str) -> Any:
        return self._config.get(key)

config = Configuration()
