from database import get_connection
from auth import generate_kt_id, generate_security_id


def create_account(telegram_id, role="user"):
    connection = get_connection()

    existing = connection.execute(
        "SELECT kt_id FROM users WHERE telegram_id = ?",
        (telegram_id,)
    ).fetchone()

    if existing:
        connection.close()
        return existing[0]

    kt_id = generate_kt_id()
    security_id = generate_security_id()

    connection.execute(
        """
        INSERT INTO users
        (telegram_id, kt_id, security_id, role)
        VALUES (?, ?, ?, ?)
        """,
        (telegram_id, kt_id, security_id, role)
    )

    connection.commit()
    connection.close()

    return kt_id
