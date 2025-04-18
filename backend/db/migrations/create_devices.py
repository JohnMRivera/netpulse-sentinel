from core import DBConnection
import psycopg2

class CreateDevices:

    def __init__(self):
        dbConnection = DBConnection()
        self.connection = dbConnection.getConnection()

    def up(self):
        sql = "CREATE TABLE devices("\
            "device_id SERIAL PRIMARY KEY,"\
            "device_name VARCHAR(50),"\
            "device_ip VARCHAR(15),"\
            "device_mac VARCHAR(50),"\
            "device_os VARCHAR(17),"\
            "device_status VARCHAR(7),"\
            "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"\
            "updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP"\
            ")"

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)

            self.connection.commit()
            self.connection.close()

            print("Tabla devices creada exitosamente")

        except psycopg2.Error as e:
            print(f"Error al intentar crear la tabla devices: {str(e)}")


    def down(self):

        sql = "DROP TABLE devices"

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)

            self.connection.commit()
            self.connection.close()

            print("Tabla devices eliminada exitosamente")

        except psycopg2.Error as e:
            print(f"Error al intentar eliminar la tabla devices: {str(e)}")