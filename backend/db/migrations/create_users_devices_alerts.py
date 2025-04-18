from core import DBConnection
import psycopg2

class CreateUsersDevicesAlerts:

    def __init__(self):
        dbConnection = DBConnection()
        self.connection = dbConnection.getConnection()

    def up(self):
        sql = "CREATE TABLE users_devices_alerts("\
            "uda_id SERIAL PRIMARY KEY,"\
            "user_id INT,"\
            "device_id INT,"\
            "alert_id INT,"\
            "is_enabled BOOLEAN,"\
            "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"\
            "updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP"\
            ")"
        
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)

            self.connection.commit()
            self.connection.close()

            print("Tabla users_devices_alerts creada exitosamente")

        except psycopg2.Error as e:
            print(f"Error al intentar crear la tabla users_devices_alerts: {str(e)}")


    def down(self):
        sql = "DROP TABLE users_devices_alerts"

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)

            self.connection.commit()
            self.connection.close()

            print("Tabla users_devices_alerts eliminada exitosamente")

        except psycopg2.Error as e:
            print(f"Error al intentar eliminar la tabla users_devices_alerts: {str(e)}")