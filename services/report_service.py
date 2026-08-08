import os
import pandas as pd
from datetime import datetime

from database.db import get_db, close_db
from config import Config


# ==========================================
# Generate CSV Report
# ==========================================
def generate_report(report_type):
    """
    Generate CSV report
    """

    tables = {

        "beneficiaries": "beneficiaries",

        "nutrition": "nutrition",

        "attendance": "attendance",

        "health": "health_checkups"

    }

    if report_type not in tables:

        return False, "Invalid Report Type"

    conn = get_db()

    if not conn:

        return False, "Database Connection Failed"

    try:

        query = f"SELECT * FROM {tables[report_type]}"

        df = pd.read_sql(query, conn)

        os.makedirs(
            Config.REPORT_FOLDER,
            exist_ok=True
        )

        filename = (

            f"{report_type}_"

            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

        )

        filepath = os.path.join(

            Config.REPORT_FOLDER,

            filename

        )

        df.to_csv(

            filepath,

            index=False

        )

        return True, {

            "filename": filename,

            "filepath": filepath,

            "rows": len(df)

        }

    except Exception as e:

        return False, str(e)

    finally:

        close_db(conn)


# ==========================================
# Read Report
# ==========================================
def read_report(filename):

    filepath = os.path.join(

        Config.REPORT_FOLDER,

        filename

    )

    if not os.path.exists(filepath):

        return None

    return pd.read_csv(filepath)