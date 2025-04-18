from core import DBConnection
import psycopg2

class CreatePermissions:

    def __init__(self):
        dbConnection = DBConnection()
        self.connection = dbConnection.getConnection()

    def up(self):
        sql = "CREATE TABLE permissions("\
            "permission_id SERIAL PRIMARY KEY,"\
            "role_id INT,"\
            "module_id INT,"\
            "permission_access INT,"\
            "created_at TIMESTAMP, "\
            "updated_at TIMESTAMP"\
            ")"
        
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)

            self.connection.commit()
            self.connection.close()

            print("Tabla permissions creada exitosamente")
        
        except psycopg2.Error as e:
            print(f"Error al intentar crear la tabla permissions: {str(e)}")

    def down(self):
        sql = "DROP TABLE permissions"

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)

            self.connection.commit()
            self.connection.close()

            print("Tabla permissions eliminada exitosamente")

        except psycopg2.Error as e:
            print(f"Error al intentar eliminar la tabla permissions: {str(e)}")