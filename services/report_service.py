from database.db import get_db, close_db


REPORT_TABLES = {
    "beneficiaries": "beneficiaries",
    "nutrition": "nutrition",
    "attendance": "attendance",
    "health": "health_checkups"
}


def generate_report(report_type):

    table_name = REPORT_TABLES.get(
        report_type
    )

    if not table_name:
        return False, "Invalid report type."

    conn = get_db()

    if not conn:
        return False, "Database connection failed."

    try:
        cursor = conn.cursor(
            dictionary=True
        )

        cursor.execute(
            f"SELECT * FROM {table_name}"
        )

        rows = cursor.fetchall()

        return True, {
            "rows": rows,
            "count": len(rows)
        }

    except Exception as e:

        print(
            f"[Report Error] {e}"
        )

        return False, str(e)

    finally:
        close_db(conn)