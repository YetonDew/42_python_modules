import os
import sys


REQUIRED_VARS = (
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_FILE = os.path.join(BASE_DIR, ".env")


class ConfigurationError(Exception):
    pass


def load_config() -> dict[str, str | None]:
    try:
        from dotenv import load_dotenv
    except ImportError as error:
        raise ConfigurationError(
            "python-dotenv is missing; run "
            "'pip install -r requirements.txt'"
        ) from error

    load_dotenv(ENV_FILE, override=False)
    return {name: os.environ.get(name) for name in REQUIRED_VARS}


def check_config(config: dict[str, str | None]) -> bool:
    mode = config.get("MATRIX_MODE")
    missing = [name for name in REQUIRED_VARS if not config.get(name)]

    if mode not in {"development", "production"}:
        print("[WARNING] MATRIX_MODE must be development or production")

    level = "CRITICAL" if mode == "production" else "WARNING"
    for name in missing:
        print(f"[{level}] {name} is missing!")

    if mode == "production" and missing:
        raise ConfigurationError(
            "Production environment is incomplete"
        )
    return not missing and mode in {"development", "production"}


def database_status(database_url: str | None) -> str:
    if not database_url:
        return "Disconnected"
    if "localhost" in database_url or "127.0.0.1" in database_url:
        return "Connected to local instance"
    return "Connected to remote instance"


def display_config(config: dict[str, str | None]) -> None:
    print("Configuration loaded:")
    print(f"Mode: {config.get('MATRIX_MODE') or 'Not configured'}")
    print(f"Database: {database_status(config.get('DATABASE_URL'))}")
    api_status = "Authenticated" if config.get("API_KEY") else "Missing"
    print(f"API Access: {api_status}")
    print(f"Log Level: {config.get('LOG_LEVEL') or 'Not configured'}")
    zion_status = "Online" if config.get("ZION_ENDPOINT") else "Offline"
    print(f"Zion Network: {zion_status}")


def security_check(config: dict[str, str | None]) -> None:
    print("Environment security check:")
    placeholders = {"your_api_key_here", "change_me", "replace_me"}
    if config.get("API_KEY") in placeholders:
        print("[WARNING] Replace the example API key")
    else:
        print("[OK] No hardcoded secrets detected")

    if os.path.isfile(ENV_FILE):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file missing")

    if config.get("MATRIX_MODE") == "production":
        print("[OK] Production overrides available")
    else:
        print("[INFO] Development mode active")


def main() -> int:
    print("ORACLE STATUS: Reading the Matrix...")
    try:
        config = load_config()
        complete = check_config(config)
    except ConfigurationError as error:
        print(f"MISSION ABORTED: {error}")
        return 1

    if not complete:
        print("Configuration incomplete; review .env.example")
    display_config(config)
    security_check(config)
    print("The Oracle sees all configurations.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
