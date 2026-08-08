from flask import (
    Blueprint,
    render_template,
    flash,
    redirect,
    url_for,
    send_from_directory
)

from config import Config
from services.report_service import generate_report

report_bp = Blueprint(
    "report",
    __name__
)


# ==========================================
# Generate Report
# ==========================================
@report_bp.route("/report/<report_type>")
def report(report_type):

    success, result = generate_report(report_type)

    if not success:

        flash(result, "danger")

        return redirect(url_for("home.home"))

    return render_template(

        "report_generated.html",

        filename=result["filename"],

        rows=result["rows"],

        report_type=report_type

    )


# ==========================================
# Download Report
# ==========================================
@report_bp.route("/download/<filename>")
def download(filename):

    return send_from_directory(

        Config.REPORT_FOLDER,

        filename,

        as_attachment=True

    )