from core import DBConnection
import psycopg2

class CreateModules:

    def __init__(self):
        dbConnection = DBConnection()
        self.connection = dbConnection.getConnection()

    def up(self):
        sql = "CREATE TABLE modules("\
            "module_id SERIAL PRIMARY KEY,"\
            "module_name VARCHAR(50)"\
            ")"
        
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)

            self.connection.commit()
            self.connection.close()

            print("Tabla modules creada exitosamente")

        except psycopg2.Error as e:
            print(f"Error al intentear crear la tabla modules: {str(e)}")

    def down(self):
        sql = "DROP TABLE modules"

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)

            self.connection.commit()
            self.connection.close()

            print("Tabla modules eliminada exitosamente")

        except psycopg2.Error as e:
            print(f"Error al intentar eliminar la tabla modules: {str(e)}")