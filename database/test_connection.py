from database.connection import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT current_user, current_database();")
print(cursor.fetchone())

cursor.close()
conn.close()