from .user import user_router
from flask import Blueprint


# Main Router Blueprint
router = Blueprint("router", __name__, url_prefix="/api/v1")


# Registering the different routers
router.register_blueprint(user_router)