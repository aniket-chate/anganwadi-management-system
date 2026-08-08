import csv

from io import StringIO, BytesIO

from flask import (
    Blueprint,
    render_template,
    flash,
    redirect,
    url_for,
    send_file
)

from services.report_service import (
    generate_report
)


report_bp = Blueprint(
    "report",
    __name__
)


# ==========================================
# Generate Report Page
# ==========================================

@report_bp.route(
    "/report/<report_type>"
)
def report(report_type):

    success, result = generate_report(
        report_type
    )

    if not success:

        flash(
            result,
            "danger"
        )

        return redirect(
            url_for("home.home")
        )

    filename = (
        f"{report_type}_report.csv"
    )

    return render_template(
        "report_generated.html",
        filename=filename,
        rows=result["count"],
        report_type=report_type
    )


# ==========================================
# Download Report
# ==========================================

@report_bp.route(
    "/download/<report_type>"
)
def download(report_type):

    success, result = generate_report(
        report_type
    )

    if not success:

        flash(
            result,
            "danger"
        )

        return redirect(
            url_for("home.home")
        )

    rows = result["rows"]

    output = StringIO()

    if rows:

        fieldnames = list(
            rows[0].keys()
        )

        writer = csv.DictWriter(
            output,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(rows)

    else:

        output.write(
            "No records found\n"
        )

    csv_bytes = BytesIO(
        output.getvalue().encode(
            "utf-8"
        )
    )

    filename = (
        f"{report_type}_report.csv"
    )

    return send_file(
        csv_bytes,
        mimetype="text/csv",
        as_attachment=True,
        download_name=filename
    )