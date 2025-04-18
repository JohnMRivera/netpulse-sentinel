from core import DBConnection
import psycopg2

class CreateDevicesLogs:

    def __init__(self):
        dbConnection = DBConnection()
        self.connection = dbConnection.getConnection()

    def up(self):
        sql = "CREATE TABLE devices_logs("\
            "d_logs_id SERIAL PRIMARY KEY,"\
            "device_id INT,"\
            "d_log_status VARCHAR(50),"\
            "triggered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP"\
            ")"
        
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)

            self.connection.commit()
            self.connection.close()

            print("Tabla devices_logs creada exitosamente")

        except psycopg2.Error as e:
            print(f"Error al intentar crear la tabla devices_logs: {str(e)}")

    def down(self):
        sql = "DROP TABLE devices_logs"

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)

            self.connection.commit()
            self.connection.close()

            print("Tabla devices_logs eliminada con exito")

        except psycopg2.Error as e:
            print(f"Error al intentar crear la tabla devices_logs: {str(e)}")