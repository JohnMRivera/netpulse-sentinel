import psycopg2

class DBConnection:

    # Se inicializa la variable connection
    def __init__(self):
        self.connection = None

    # Función para obtener la conexión a la base de datos
    def getConnection(self):
        try:
            # Se establece la conexión a la base de datos
            self.connection = psycopg2.connect(
                user="nps_admin",
                password="NPS dfpsc3108 .",
                host="localhost",
                database="nps_db"
            )

            # Se devuelve la conexión
            return self.connection
        
        except Exception as e:
            print(f"Error al obtener la conexión con la base de datos: {e}")

            return None

    # Función para cerrar la conexión a la base de datos
    def closeConnection(self):
        try:
            # Si la conexión es válida, se cierra
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