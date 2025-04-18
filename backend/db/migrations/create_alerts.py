from core import DBConnection
import psycopg2

class CreateAlerts:

    def __init__(self):
        dbConnection = DBConnection()
        self.connection = dbConnection.getConnection()

    def up(self):
        sql = "CREATE TABLE alerts("\
            "alert_id SERIAL PRIMARY KEY,"\
            "alert_name VARCHAR(50),"\
            "alert_type VARCHAR(50),"\
            "alert_threshold VARCHAR(50),"\
            "alert_description TEXT,"\
            "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"\
            "updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP"\
            ")"

        statusmessage = None

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)

                statusmessage = cursor.statusmessage

            self.connection.commit()
            self.connection.close()

            print(statusmessage)

            print("Tabla alerts creada exitosamente")

        except psycopg2.Error as e:
            print(f"Error al intentar crear la tabla alerts: {str(e)}")

    def down(self):
        sql = "DROP TABLE alerts"

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)

            self.connection.commit()
            self.connection.close()

            print("Tabla alerts eliminada exitosamente")

        except psycopg2.Error as e:
            print(f"Error al intentar eliminar la tabla alerts: {str(e)}")