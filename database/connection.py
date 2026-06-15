import psycopg2


def get_connection():
    return psycopg2.connect(
        host="127.0.0.1",
        port=5433,
        database="siem_db",
        user="siem",
        password="siem_password"
    )