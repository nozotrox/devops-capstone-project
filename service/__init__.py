"""
Package: service
Package for the application models and service routes
This module creates and configures the Flask app and sets up the logging
and SQL database
"""
import sys
from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS
from service import config
from service.common import log_handlers

# Create Flask application
app = Flask(__name__)
app.config.from_object(config)

# Initialize Flask-Talisman for security headers
talisman = Talisman(
    app,
    force_https=app.config.get('TALISMAN_FORCE_HTTPS', False),
    force_https_permanent_redirects=app.config.get('TALISMAN_FORCE_HTTPS_PERMANENT_REDIRECTS', True),
    strict_transport_security=app.config.get('TALISMAN_STRICT_TRANSPORT_SECURITY', True),
    strict_transport_security_max_age=app.config.get('TALISMAN_STRICT_TRANSPORT_SECURITY_MAX_AGE', 31536000),
    content_security_policy=app.config.get('TALISMAN_CONTENT_SECURITY_POLICY', {}),
    content_security_policy_nonce_in=['script-src']
)

# Initialize Flask-CORS for cross-origin resource sharing
CORS(
    app,
    origins=app.config.get('CORS_ORIGINS', ['*']),
    methods=app.config.get('CORS_METHODS', ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']),
    allow_headers=app.config.get('CORS_ALLOW_HEADERS', ['Content-Type', 'Authorization', 'X-Requested-With']),
    expose_headers=app.config.get('CORS_EXPOSE_HEADERS', ['Content-Type', 'X-Total-Count']),
    supports_credentials=app.config.get('CORS_SUPPORTS_CREDENTIALS', True),
    max_age=app.config.get('CORS_MAX_AGE', 3600)
)

# Import the routes After the Flask app is created
# pylint: disable=wrong-import-position, cyclic-import, wrong-import-order
from service import routes, models  # noqa: F401 E402

# pylint: disable=wrong-import-position
from service.common import error_handlers, cli_commands  # noqa: F401 E402

# Set up logging for production
log_handlers.init_logging(app, "gunicorn.error")

app.logger.info(70 * "*")
app.logger.info("  A C C O U N T   S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")

try:
    models.init_db(app)  # make our database tables
except Exception as error:  # pylint: disable=broad-except
    app.logger.critical("%s: Cannot continue", error)
    # gunicorn requires exit code 4 to stop spawning workers when they die
    sys.exit(4)

app.logger.info("Service initialized!")
