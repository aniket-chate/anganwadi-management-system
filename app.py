from flask import Flask, render_template

from config import Config

from routes.home_routes import home_bp
from routes.beneficiary_routes import beneficiary_bp
from routes.report_routes import report_bp


# ==========================================
# Flask Application
# ==========================================

app = Flask(__name__)

# Load configuration
app.config.from_object(Config)


# ==========================================
# Register Blueprints
# ==========================================

app.register_blueprint(home_bp)
app.register_blueprint(beneficiary_bp)
app.register_blueprint(report_bp)


# ==========================================
# Error Handlers
# ==========================================

@app.errorhandler(404)
def page_not_found(error):
    return render_template(
        "404.html"
    ), 404


@app.errorhandler(500)
def internal_error(error):

    # Print the actual exception to Vercel Runtime Logs
    # while keeping the user-facing error page clean.
    import traceback

    print("=" * 70)
    print("INTERNAL SERVER ERROR")
    print("=" * 70)

    traceback.print_exc()

    print("ERROR:", error)

    print("=" * 70)

    return render_template(
        "500.html"
    ), 500


# ==========================================
# Local Development
# ==========================================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )