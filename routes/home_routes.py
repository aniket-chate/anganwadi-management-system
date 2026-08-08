from flask import Blueprint, render_template

from services.beneficiary_service import get_total_beneficiaries

home_bp = Blueprint(
    "home",
    __name__
)


@home_bp.route("/")
def home():

    return render_template(

    "index.html",

    total_beneficiaries=get_total_beneficiaries(),

    total_reports=4

)
    