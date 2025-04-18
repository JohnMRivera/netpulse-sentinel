from core import DBConnection
import psycopg2

class CreateRoles:

    def __init__(self):
        dbConnection = DBConnection()
        self.connection = dbConnection.getConnection()

    def up(self):
        sql = "CREATE TABLE roles("\
            "role_id SERIAL PRIMARY KEY,"\
            "role_name VARCHAR(50),"\
            "created_at TIMESTAMP,"\
            "updated_at TIMESTAMP"\
            ")"

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)

            self.connection.commit()
            self.connection.close()

            print("Tabla roles creada exitosamente")

        except psycopg2.Error as e:
            print(f"Error al intentar crear la tabla roles: {str(e)}")

    def down(self):
        sql = "DROP TABLE roles"

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)

            self.connection.commit()
            self.connection.close()

            print("Tabla roles eliminada exitosamente")

        except psycopg2.Error as e:
            print(f"Error al intentar crear la tabla roles: {str(e)}")