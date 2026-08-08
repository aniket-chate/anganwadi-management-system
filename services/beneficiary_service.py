from database.db import get_db, close_db


# ==========================================
# Get All Beneficiaries
# ==========================================

def get_all_beneficiaries():

    conn = get_db()

    if not conn:
        return []

    try:
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT
                id,
                beneficiary_name,
                age,
                category,
                health_status
            FROM beneficiaries
            ORDER BY beneficiary_name
        """)

        return cursor.fetchall()

    except Exception as e:
        print(f"[Get Beneficiaries Error] {e}")
        return []

    finally:
        close_db(conn)


# ==========================================
# Get Beneficiary By ID
# ==========================================

def get_beneficiary_by_id(beneficiary_id):

    conn = get_db()

    if not conn:
        return None

    try:
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT
                id,
                beneficiary_name,
                age,
                category,
                health_status
            FROM beneficiaries
            WHERE id = %s
        """, (beneficiary_id,))

        return cursor.fetchone()

    except Exception as e:
        print(f"[Get Beneficiary Error] {e}")
        return None

    finally:
        close_db(conn)


# ==========================================
# Add Beneficiary
# ==========================================

def add_beneficiary(
    name,
    age,
    category,
    health_status
):

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
        """, (
            name,
            age,
            category,
            health_status
        ))

        conn.commit()

        return True

    except Exception as e:
        print(f"[Add Beneficiary Error] {e}")

        try:
            conn.rollback()
        except Exception:
            pass

        return False

    finally:
        close_db(conn)


# ==========================================
# Update Beneficiary
# ==========================================

def update_beneficiary(
    beneficiary_id,
    health_status
):

    conn = get_db()

    if not conn:
        return False

    try:
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE beneficiaries
            SET health_status = %s
            WHERE id = %s
        """, (
            health_status,
            beneficiary_id
        ))

        conn.commit()

        return cursor.rowcount > 0

    except Exception as e:
        print(f"[Update Beneficiary Error] {e}")

        try:
            conn.rollback()
        except Exception:
            pass

        return False

    finally:
        close_db(conn)


# ==========================================
# Delete Beneficiary
# ==========================================

def delete_beneficiary(beneficiary_id):

    conn = get_db()

    if not conn:
        return False

    try:
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM beneficiaries
            WHERE id = %s
        """, (beneficiary_id,))

        conn.commit()

        return cursor.rowcount > 0

    except Exception as e:
        print(f"[Delete Beneficiary Error] {e}")

        try:
            conn.rollback()
        except Exception:
            pass

        return False

    finally:
        close_db(conn)


# ==========================================
# Search Beneficiaries
# ==========================================

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
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT
                id,
                beneficiary_name,
                age,
                category,
                health_status
            FROM beneficiaries
            WHERE 1 = 1
        """

        params = []

        if name:
            query += """
                AND beneficiary_name LIKE %s
            """
            params.append(f"%{name}%")

        if category and category != "All":
            query += """
                AND category = %s
            """
            params.append(category)

        if health_status:
            query += """
                AND health_status LIKE %s
            """
            params.append(
                f"%{health_status}%"
            )

        valid_sort = {
            "name": "beneficiary_name",
            "age": "age",
            "category": "category"
        }

        sort_column = valid_sort.get(
            sort,
            "beneficiary_name"
        )

        query += f"""
            ORDER BY {sort_column}
        """

        cursor.execute(
            query,
            params
        )

        return cursor.fetchall()

    except Exception as e:
        print(f"[Search Error] {e}")
        return []

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

        cursor.execute("""
            SELECT COUNT(*)
            FROM beneficiaries
        """)

        result = cursor.fetchone()

        return result[0] if result else 0

    except Exception as e:
        print(f"[Beneficiary Count Error] {e}")
        return 0

    finally:
        close_db(conn)


def get_total_health_records():

    conn = get_db()

    if not conn:
        return 0

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(*)
            FROM health_checkups
        """)

        result = cursor.fetchone()

        return result[0] if result else 0

    except Exception as e:
        print(f"[Health Count Error] {e}")
        return 0

    finally:
        close_db(conn)


def get_total_attendance():

    conn = get_db()

    if not conn:
        return 0

    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT COUNT(*)
            FROM attendance
        """)

        result = cursor.fetchone()

        return result[0] if result else 0

    except Exception as e:
        print(f"[Attendance Count Error] {e}")
        return 0

    finally:
        close_db(conn)