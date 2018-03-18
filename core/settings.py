import os

# Define static and templates paths for the app
BASE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
CONTRACT_DIR = os.path.join(BASE_DIR, 'contracts')


class Common:
    """
    Common settings class. All children inherit from this one.
    """
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')


class Dev(Common):
    """
    Development settings for local development.
    """
    DEBUG = True
    TESTING = True


class Prod(Common):
    """
    Product settings.
    """
    DEBUG = False
