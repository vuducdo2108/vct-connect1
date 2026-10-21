import os
from pathlib import Path
from .migrations import apply_migrations


if __name__ == "__main__":
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        env_file = Path(".env")
        if env_file.exists():
            for line in env_file.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line.startswith("DATABASE_URL="):
                    db_url = line.split("=", 1)[1].strip()
                    break
    if not db_url:
        raise KeyError("DATABASE_URL environment variable is not set and not found in .env")
    apply_migrations(db_url)
