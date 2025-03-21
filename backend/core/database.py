import psycopg2

class DBConnection:

    def __init__(self):
        self.connection = None

    def getConnection(self):
        try:
            self.connection = psycopg2.connect(
                user="nps_admin",
                password="NPS dfpsc3108 .",
                host="localhost",
                database="nps_db"
            )

            print("Conexión exitosa")

            return self.connection
        
        except Exception as e:
            print(f"Error al obtener la conexión con la base de datos: {e}")

            return None

    def closeConnection(self):
        try:
            if self.connection:
                self.connection.close()

                print("Conexión cerrada con exito")

                return True
            
            else:
                print("No hay una conexión activa para cerrar")

                return False
        
        except Exception as e:
            print(f"Error al cerrar la conexión: {e}")

            return False