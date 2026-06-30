"""Topic 41: environment variables."""


import os


# Environment-variable thinking:
# Some values should not be hard-coded into code, especially secrets or
# machine-specific settings.
#
# Environment variables let the outside system provide those values.
app_mode = os.environ.get("APP_MODE", "development")
debug_enabled = os.environ.get("DEBUG", "false").lower() == "true"

print(f"App mode: {app_mode}")
print(f"Debug enabled: {debug_enabled}")


def get_database_url():
    # Use a safe default for learning.
    # In a real app, a database URL might come from the server environment.
    return os.environ.get("DATABASE_URL", "sqlite:///local.db")


print(f"Database URL: {get_database_url()}")

# Important:
# Do not commit real passwords, tokens, or secret keys.
# Put secret values in environment variables or ignored `.env` files.

print(f"Has debug setting? {'DEBUG' in os.environ}")
