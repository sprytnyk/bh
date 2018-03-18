import os

from flask import Flask

try:
    from core import local_settings as settings
except ImportError:
    from core import settings

__version__ = '1.0.0'


def create_app():
    """
    This function creates application with predefined settings that depends on
    environment variable of a system.
    :return: application
    """
    application = Flask(
        __name__,
        template_folder=settings.TEMPLATE_DIR,
        static_folder=settings.STATIC_DIR
    )
    environment = os.environ.get('APP_ENV', 'dev')
    environments = {
        'dev': settings.Dev,
        'prod': settings.Prod
    }
    if environment in environments:
        application.config.from_object(environments[environment])
    else:
        raise EnvironmentError('Application variable has not been specified.')

    # Register blueprints
    from app.views import app_bp
    application.register_blueprint(app_bp)

    return application
