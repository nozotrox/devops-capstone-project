"""
Global Configuration for Application
"""
import os


# Get configuration from environment
DATABASE_URI = os.getenv("DATABASE_URI")

# Build DATABASE_URI from environment if not found
if not DATABASE_URI:
    DATABASE_USER = os.getenv("DATABASE_USER", "postgres")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "postgres")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "postgres")
    DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
    DATABASE_URI = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:5432/{DATABASE_NAME}"

# Configure SQLAlchemy
SQLALCHEMY_DATABASE_URI = DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Secret for session management
SECRET_KEY = os.getenv("SECRET_KEY", "s3cr3t-key-shhhh")

# Security Configuration
# Flask-Talisman settings
TALISMAN_FORCE_HTTPS = os.getenv("TALISMAN_FORCE_HTTPS", "false").lower() == "true"
TALISMAN_FORCE_HTTPS_PERMANENT_REDIRECTS = True
TALISMAN_STRICT_TRANSPORT_SECURITY = True
TALISMAN_STRICT_TRANSPORT_SECURITY_MAX_AGE = 31536000  # 1 year
TALISMAN_CONTENT_SECURITY_POLICY = {
    'default-src': ["'self'"],
    'script-src': ["'self'", "'unsafe-inline'"],
    'style-src': ["'self'", "'unsafe-inline'"],
    'img-src': ["'self'", "data:", "https:"],
    'font-src': ["'self'"],
    'connect-src': ["'self'"],
    'frame-ancestors': ["'none'"],
    'base-uri': ["'self'"],
    'form-action': ["'self'"]
}

# CORS Configuration
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")
CORS_METHODS = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
CORS_ALLOW_HEADERS = ["Content-Type", "Authorization", "X-Requested-With"]
CORS_EXPOSE_HEADERS = ["Content-Type", "X-Total-Count"]
CORS_SUPPORTS_CREDENTIALS = True
CORS_MAX_AGE = 3600  # 1 hour
