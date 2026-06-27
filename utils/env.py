from pathlib import Path
from dotenv import load_dotenv

def load_project_env():
    current = Path(__file__).resolve()
    for parent in [current.parent] + list(current.parents):
        env_file = parent / ".env"
        if env_file.exists():
            print("Loading environment from", env_file)
            load_dotenv(str(env_file))
            load_dotenv(env_file, override=True)
            return env_file

    raise FileNotFoundError("Could not find .env")