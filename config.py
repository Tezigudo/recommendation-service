# config.py
import os
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8888")
RECOMMENDER_PORT = int(os.getenv("RECOMMENDER_PORT", 8000))
_origins_raw = os.getenv("ALLOWED_ORIGINS", "")
ALLOWED_ORIGINS = [o.strip() for o in _origins_raw.split(",") if o.strip()] if _origins_raw else []
# When origins contains '*', allow_credentials must be False (browsers reject credentialed wildcard).
CORS_ALLOW_CREDENTIALS = "*" not in ALLOWED_ORIGINS
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
# Shared secret for internal-only access to /recommend. When set, the endpoint
# requires a matching X-Internal-Token header (sent by the backend). Empty =
# open (local dev).
INTERNAL_TOKEN = os.getenv("INTERNAL_TOKEN", "")
