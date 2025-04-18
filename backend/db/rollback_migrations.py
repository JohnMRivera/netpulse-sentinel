from core.database import DBConnection
import os

DOWN_MIGRATIONS_DIR = "db/migrations/down"

dbConnection = DBConnection()
connection = dbConnection.getConnection()

print(os.path.join(DOWN_MIGRATIONS_DIR, "rollback.sql"))
file = open(os.path.join(DOWN_MIGRATIONS_DIR, "rollback.sql"), "r")
content_file = file.read()

print(content_file)

try:
    with connection.cursor() as cursor:
        cursor.execute(content_file)

        rows_count = cursor.rowcount

    connection.commit()
    dbConnection.closeConnection()

    print(f"Tablas eliminadas")

except Exception as e:
    print(f"Error al intentar ejecutar el rollback: {str(e)}")