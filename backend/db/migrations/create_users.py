from core import DBConnection
import psycopg2

class CreateUsers:

    def __init__(self):
        dbConnection = DBConnection()
        self.connection = dbConnection.getConnection()

    def up(self):
        sql = "CREATE TABLE users("\
            "user_id SERIAL PRIMARY KEY,"\
            "role_id INT,"\
            "user_firstname VARCHAR(50),"\
            "user_lastname VARCHAR(50),"\
            "user_email VARCHAR(50),"\
            "user_passwd VARCHAR(50),"\
            "user_status VARCHAR(7),"\
            "created_at TIMESTAMP,"\
            "updated_at TIMESTAMP"\
            ")"
        
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql,)

                rowcount = cursor.rowcount

            self.connection.commit()
            self.connection.close()

            print("Tabla users creada exitosamente")

        except psycopg2.Error as e:
            print(f"Error al intentar crear la tabla users: {str(e)}")
    
    def down(self):
        sql = "DROP TABLE users"

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)

                rowcount = cursor.rowcount

            self.connection.commit()
            self.connection.close()

            print("Tabla users eliminada exitosamente")

        except psycopg2.Error as e:
            print(f"Error al intentar crear la tabla users: {str(e)}")