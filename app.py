from flask import Flask
from config import Config
from flask import render_template

# Import Blueprints
from routes.home_routes import home_bp
from routes.beneficiary_routes import beneficiary_bp
from routes.report_routes import report_bp


def create_app():
    app = Flask(__name__)

    # Load Configuration
    app.config.from_object(Config)

    # Register Blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(beneficiary_bp)
    app.register_blueprint(report_bp)

   
    @app.errorhandler(404)
    def page_not_found(error):

        return render_template(
            "404.html"
        ), 404


    @app.errorhandler(500)
    def internal_error(error):

        return render_template(
            "500.html"
        ), 500

    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )