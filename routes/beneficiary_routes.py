from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from services.beneficiary_service import (
    get_all_beneficiaries,
    get_beneficiary_by_id,
    add_beneficiary,
    update_beneficiary,
    delete_beneficiary,
    search_beneficiaries
)

beneficiary_bp = Blueprint(
    "beneficiary",
    __name__
)


# ======================================
# View All Beneficiaries
# ======================================
@beneficiary_bp.route("/beneficiaries")
def beneficiaries():

    beneficiaries = get_all_beneficiaries()

    return render_template(
        "beneficiaries.html",
        beneficiaries=beneficiaries
    )


# ======================================
# Add Beneficiary
# ======================================
@beneficiary_bp.route(
    "/beneficiary/add",
    methods=["POST"]
)
def add():

    try:
        name = request.form.get("name", "").strip()
        age = request.form.get("age", "").strip()
        category = request.form.get("category", "").strip()
        health_status = request.form.get("health_status", "").strip()

        # Validate form data
        if not all([
            name,
            age,
            category,
            health_status
        ]):
            flash(
                "Please fill all fields.",
                "danger"
            )

            return redirect(
                url_for("home.home"),
                code=303
            )

        # Validate age
        try:
            age = int(age)

            if age < 0:
                raise ValueError

        except (ValueError, TypeError):

            flash(
                "Please enter a valid age.",
                "danger"
            )

            return redirect(
                url_for("home.home"),
                code=303
            )

        # Insert into database
        success = add_beneficiary(
            name,
            age,
            category,
            health_status
        )

        if success:

            flash(
                "Beneficiary Added Successfully.",
                "success"
            )

        else:

            flash(
                "Failed to Add Beneficiary.",
                "danger"
            )

        # Use 303 after POST.
        # This explicitly tells the browser to perform
        # a GET request after the successful POST.
        return redirect(
            url_for("beneficiary.beneficiaries"),
            code=303
        )

    except Exception as e:

        print(
            f"[Add Route Error] {e}"
        )

        flash(
            "An unexpected error occurred while adding the beneficiary.",
            "danger"
        )

        return redirect(
            url_for("home.home"),
            code=303
        )


# ======================================
# Update Form
# ======================================
@beneficiary_bp.route(
    "/beneficiary/edit/<int:id>"
)
def edit(id):

    beneficiary = get_beneficiary_by_id(id)

    if not beneficiary:

        flash("Beneficiary Not Found.", "warning")

        return redirect(
            url_for("beneficiary.beneficiaries")
        )

    return render_template(
        "update.html",
        beneficiary=beneficiary
    )


# ======================================
# Update Beneficiary
# ======================================
@beneficiary_bp.route(
    "/beneficiary/update/<int:id>",
    methods=["POST"]
)
def update(id):

    health_status = request.form.get(
        "health_status"
    )

    success = update_beneficiary(
        id,
        health_status
    )

    if success:

        flash(
            "Health Status Updated.",
            "success"
        )

    else:

        flash(
            "Update Failed.",
            "danger"
        )

    return redirect(
        url_for("beneficiary.beneficiaries")
    )


# ======================================
# Delete Beneficiary
# ======================================
@beneficiary_bp.route(
    "/beneficiary/delete/<int:id>"
)
def delete(id):

    success = delete_beneficiary(id)

    if success:

        flash(
            "Beneficiary Deleted.",
            "success"
        )

    else:

        flash(
            "Delete Failed.",
            "danger"
        )

    return redirect(
        url_for("beneficiary.beneficiaries")
    )


# ======================================
# Search
# ======================================
@beneficiary_bp.route("/search")
def search():

    beneficiaries = search_beneficiaries(

        name=request.args.get("name", ""),

        category=request.args.get(
            "category",
            "All"
        ),

        health_status=request.args.get(
            "health_status",
            ""
        ),

        sort=request.args.get(
            "sort",
            "name"
        )

    )

    return render_template(

        "beneficiaries.html",

        beneficiaries=beneficiaries

    )