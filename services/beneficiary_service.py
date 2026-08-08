from database.db import get_db, close_db


# ===============================
# Get All Beneficiaries
# ===============================
def get_all_beneficiaries():

    conn = get_db()

    if not conn:
        return None

    try:

        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT *
            FROM beneficiaries
            ORDER BY beneficiary_name
        """)

        return cursor.fetchall()

    finally:

        close_db(conn)


# ===============================
# Get Beneficiary By ID
# ===============================
def get_beneficiary_by_id(beneficiary_id):

    conn = get_db()

    if not conn:
        return None

    try:

        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT *
            FROM beneficiaries
            WHERE id=%s
        """, (beneficiary_id,))

        return cursor.fetchone()

    finally:

        close_db(conn)


# ===============================
# Add Beneficiary
# ===============================
def add_beneficiary(name, age, category, health_status):

    conn = get_db()

    if not conn:
        return False

    try:

        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO beneficiaries
            (
                beneficiary_name,
                age,
                category,
                health_status
            )

            VALUES
            (
                %s,
                %s,
                %s,
                %s
            )
        """,

        (
            name,
            age,
            category,
            health_status
        ))

        conn.commit()

        return True

    except Exception:

        conn.rollback()

        return False

    finally:

        close_db(conn)


# ===============================
# Update Beneficiary
# ===============================
def update_beneficiary(beneficiary_id, health_status):

    conn = get_db()

    if not conn:
        return False

    try:

        cursor = conn.cursor()

        cursor.execute("""

            UPDATE beneficiaries

            SET health_status=%s

            WHERE id=%s

        """,

        (
            health_status,
            beneficiary_id
        ))

        conn.commit()

        return cursor.rowcount > 0

    except Exception:

        conn.rollback()

        return False

    finally:

        close_db(conn)


# ===============================
# Delete Beneficiary
# ===============================
def delete_beneficiary(beneficiary_id):

    conn = get_db()

    if not conn:
        return False

    try:

        cursor = conn.cursor()

        cursor.execute("""

            DELETE FROM beneficiaries

            WHERE id=%s

        """,

        (
            beneficiary_id,
        ))

        conn.commit()

        return cursor.rowcount > 0

    except Exception:

        conn.rollback()

        return False

    finally:

        close_db(conn)


# ===============================
# Search Beneficiaries
# ===============================
def search_beneficiaries(
        name="",
        category="All",
        health_status="",
        sort="name"
):

    conn = get_db()

    if not conn:
        return []

    try:

        query = """

            SELECT *

            FROM beneficiaries

            WHERE 1=1

        """

        params = []

        if name:

            query += " AND beneficiary_name LIKE %s"

            params.append(f"%{name}%")

        if category != "All":

            query += " AND category=%s"

            params.append(category)

        if health_status:

            query += " AND health_status LIKE %s"

            params.append(f"%{health_status}%")

        valid_sort = {

            "name": "beneficiary_name",
            "age": "age",
            "category": "category"

        }

        query += f" ORDER BY {valid_sort.get(sort,'beneficiary_name')}"

        cursor = conn.cursor(dictionary=True)

        cursor.execute(query, params)

        return cursor.fetchall()

    finally:

        close_db(conn)
        
# ==========================================
# Dashboard Statistics
# ==========================================

def get_total_beneficiaries():

    conn = get_db()

    if not conn:
        return 0

    try:

        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM beneficiaries")

        return cursor.fetchone()[0]

    finally:

        close_db(conn)


def get_total_health_records():

    conn = get_db()

    if not conn:
        return 0

    try:

        cursor = conn.cursor()

        # Change table name if different
        cursor.execute("SELECT COUNT(*) FROM health_checkups")

        return cursor.fetchone()[0]

    finally:

        close_db(conn)


def get_total_attendance():

    conn = get_db()

    if not conn:
        return 0

    try:

        cursor = conn.cursor()

        # Change table name if different
        cursor.execute("SELECT COUNT(*) FROM attendance")

        return cursor.fetchone()[0]

    finally:

        close_db(conn)