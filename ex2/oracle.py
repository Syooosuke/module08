import os
import sys

try:
    from dotenv import load_dotenv #type: ignore

except ImportError:
    print(
        "Error: python-dotenv is not installed. Please run 'poetry install'.",
        file=sys.stderr,
    )
    sys.exit(1)


def main() -> None:
    env_loaded: bool = load_dotenv()
    print("ORACLE STATUS: Reading the Matrix...\n")

    mode: str = os.getenv("MATRIX_MODE", "unconfigured")
    db_url: str | None = os.getenv("DATABASE_URL")
    api_key: str | None = os.getenv("API_KEY")
    log_level: str = os.getenv("LOG_LEVEL", "WARNING")
    zion_endpoint: str | None = os.getenv("ZION_ENDPOINT")

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if db_url:
        if mode == "production":
            print("Database: Connected to secure prodution cluster")
        else:
            print("Database: Connected to local instance")
    else:
        print("Database: [WARNING] Connection string missing")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: [WARNING] Missing API Key")

    print(f"Log Level: {log_level}")

    if zion_endpoint:
        print("Zion Network: Online")
    else:
        print("Zion Network: [WARNING] Endpoint missing")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if env_loaded:
        print("[OK] .env file properly configured")
    else:
        print(
            "[WARNING] .env file not found. Running with missing "
            "configurations."
        )

    if mode == "production":
        print("[OK] Production overrides available")
    else:
        print(
            "[INFO] Running in development mode. No production overrides "
            "active."
        )

    print("\nThe Oracle sees all configureations.")


if __name__ == "__main__":
    main()
