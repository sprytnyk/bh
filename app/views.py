from flask import Blueprint

app_bp = Blueprint('app', __name__)


@app_bp.route('/')
def home():
    pass
