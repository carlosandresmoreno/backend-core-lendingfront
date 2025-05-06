from flask import Blueprint
# from app.controllers.user_controller import user_blueprint
from app.controllers.loan_controller import loan_blueprint

def register_blueprints(app):
    # app.register_blueprint(user_blueprint, url_prefix='/api/users')
    app.register_blueprint(loan_blueprint, url_prefix='/api/loans')
