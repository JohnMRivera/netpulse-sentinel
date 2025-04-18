from core import DBConnection
import psycopg2

class CreateAlertsLogs:

    def __init__(self):
        dbConnection = DBConnection()
        self.connection = dbConnection.getConnection()

    def up(self):
        sql = "CREATE TABLE alerts_logs("\
            "a_log_id SERIAL PRIMARY KEY,"\
            "uda_id INT,"\
            "a_log_message VARCHAR(150),"\
            "triggered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP"\
            ")"
        
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)

            self.connection.commit()
            self.connection.close()

            print("Tabla alerts_logs creada exitosamente")

        except psycopg2.Error as e:
            print(f"Error al intentar crear la tabla alerts_logs: {str(e)}")

    def down(self):
        sql = "DROP TABLE alerts_logs"

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)

            self.connection.commit()
            self.connection.close()

            print("Tabla alerts_logs eliminada exitosamente")

        except psycopg2.Error as e:
            print(f"Error al intentar eliminar la tabla alerts_logs: {str(e)}")