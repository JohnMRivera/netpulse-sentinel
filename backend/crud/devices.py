from core.database import DBConnection
from models.device import Device

class DevicesCRUD:

    @staticmethod
    # Función para crear un dispositivo
    def create(device_ip, device_mac, device_status):
        dbConnection = DBConnection()
        connection = dbConnection.getConnection()

        # SQL para insertar un nuevo dispositivo, se usa RETURNING para obtener el id del dispositivo creado
        sql = "INSERT INTO devices(device_ip, device_mac, device_status)values(%s,%s,%s) RETURNING device_id"

        row = None
        
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, (device_ip, device_mac, device_status))

                # Obtenemos el id del dispositivo creado
                row = cursor.fetchone()

            connection.commit()
            dbConnection.closeConnection()

            # Si se obtuvo el id del dispositivo creado, se crea un objeto Device y se retorna
            return Device(row[0], device_ip, device_mac, device_status)

        except Exception as e:
            print(e)

            return None

    @staticmethod
    # Función para obtener un dispositivo por su id
    def getByID(device_id):
        dbConnection = DBConnection()
        connection = dbConnection.getConnection()

        # SQL para obtener un dispositivo por su id
        sql = "SELECT * FROM devices WHERE device_id = %s"

        row = None

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, (str(device_id),))

                # Obtenemos el dispositivo por su id
                row = cursor.fetchone()

            dbConnection.closeConnection()

            # Si se obtuvo el dispositivo, se crea un objeto Device y se retorna
            if(row):
                return Device(row[0], row[1], row[2], row[3])
            
            return {}

        except Exception as e:
            print(e)

            return None

    @staticmethod
    # Función para obtener un dispositivo por su ip
    def getByIP(device_ip):
        dbConnection = DBConnection()
        connection = dbConnection.getConnection()

        # SQL para obtener un dispositivo por su ip
        sql = "SELECT * FROM devices WHERE device_ip = %s"

        row = None

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, (device_ip,))
                
                # Obtenemos el dispositivo por su ip
                row = cursor.fetchone()

            dbConnection.closeConnection()

            # Si se obtuvo el dispositivo, se crea un objeto Device y se retorna
            if(row):
                return Device(row[0], row[1], row[2], row[3])
            
            return {}
        
        except Exception as e:
            print(e)

            return None

    @staticmethod
    # Función para obtener un dispositivo por su mac
    def getByMAC(device_mac):
        dbConnection = DBConnection()
        connection = dbConnection.getConnection()

        # SQL para obtener un dispositivo por su mac
        sql = "SELECT * FROM devices WHERE device_mac = %s"

        row = None

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, (device_mac,))

                # Obtenemos el dispositivo por su mac
                row = cursor.fetchone()

            dbConnection.closeConnection()

            # Si se obtuvo el dispositivo, se crea un objeto Device y se retorna
            if(row):
                return Device(row[0], row[1], row[2], row[3])
            
            return {}

        except Exception as e:
            print(e)

            return None

    @staticmethod
    # Función para obtener un dispositivo por su estado
    def getByStatus(device_status):
        dbConnection = DBConnection()
        connection = dbConnection.getConnection()

        # SQL para obtener un dispositivo por su estado
        sql = "SELECT * FROM devices WHERE device_status = %s"

        rows = None

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, (device_status,))
                
                # Obtenemos el dispositivo por su estado
                rows = cursor.fetchall()

            dbConnection.closeConnection()


            devices = []

            # Se agrega un objeto Device por cada fila obtenida a la lista devices y se retorna
            for row in rows:
                devices += [Device(row[0], row[1], row[2], row[3])]

            return devices

        except Exception as e:
            print(e)

            return None

    @staticmethod
    # Función para obtener todos los dispositivos
    def getAll():
        dbConnection = DBConnection()
        connection = dbConnection.getConnection()

        # SQL para obtener todos los dispositivos
        sql = "SELECT * FROM devices"

        rows = None

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)

                # Obtenemos todos los dispositivos
                rows = cursor.fetchall()

            dbConnection.closeConnection()

            devices = []

            # Se agrega un objeto Device por cada fila obtenida a la lista devices y se retorna
            for row in rows:
                devices += [Device(row[0], row[1], row[2], row[3])]

            return devices

        except Exception as e:
            print(e)

            return None

    @staticmethod
    # Función para actualizar un dispositivo por su id
    def updateByID(device_id, device_ip, device_mac, device_status):
        dbConnection = DBConnection()
        connection = dbConnection.getConnection()

        # SQL para actualizar un dispositivo por su id
        sql = "UPDATE devices SET device_ip = %s, device_mac = %s, device_status = %s WHERE device_id = %s"

        updated_rows = 0

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, (device_ip, device_mac, device_status, device_id))

                # Obtenemos el número de filas actualizadas
                updated_rows = cursor.rowcount

            connection.commit()
            dbConnection.closeConnection()

            # Si se actualizaron filas, se crea un objeto Device y se retorna
            if(updated_rows > 0):
                return Device(device_id, device_ip, device_mac, device_status)

            return False

        except Exception as e:
            print(e)

            return None

    @staticmethod
    # Función para eliminar un dispositivo por su id
    def deleteByID(device_id):
        dbConnection = DBConnection()
        connection = dbConnection.getConnection()

        # SQL para eliminar un dispositivo por su id
        sql = "DELETE FROM devices WHERE device_id = %s"

        deleted_rows = 0

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, (str(device_id),))

                # Obtenemos el número de filas eliminadas
                deleted_rows = cursor.rowcount
                
            connection.commit()
            dbConnection.closeConnection()

            # Si se eliminaron filas, se retorna True
            if(deleted_rows):
                return True
            
            return False

        except Exception as e:
            print(e)

            return None

    @staticmethod
    # Función para eliminar un dispositivo por su ip
    def deleteAll():
        dbConnection = DBConnection()
        connection = dbConnection.getConnection()

        # SQL para eliminar todos los dispositivos
        sql = "DELETE FROM devices"

        deleted_rows = 0

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)

                # Obtenemos el número de filas eliminadas
                deleted_rows = cursor.rowcount

            connection.commit()
            dbConnection.closeConnection()

            # Si se eliminaron filas, se retorna el número de filas eliminadas
            return deleted_rows

        except Exception as e:
            print(e)

            return None

    @staticmethod
    # Función para contar el número de dispositivos
    def countDevices():
        dbConnection = DBConnection()
        connection = dbConnection.getConnection()

        # SQL para contar el número de dispositivos
        sql = "SELECT COUNT(*) FROM devices"

        rows_count = 0

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)

                # Obtenemos el número de filas
                rows_count = cursor.fetchone()[0]

            dbConnection.closeConnection()

            # Si se obtuvo el número de filas, se retorna
            return rows_count
        
        except Exception as e:
            print(e)

            return None

    @staticmethod
    # Función para verificar si un dispositivo existe por su ip o mac
    def deviceExists(device_ip, device_mac):
        dbConnection = DBConnection()
        connection = dbConnection.getConnection()

        # SQL para verificar si un dispositivo existe por su ip o mac
        sql = "SELECT * FROM devices WHERE device_ip = %s OR device_mac = %s"

        row = None

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, (device_ip, device_mac))

                # Obtenemos el dispositivo por su ip o mac
                row = cursor.fetchone()

            dbConnection.closeConnection()

            # Si se obtuvo el dispositivo, se crea un objeto Device y se retorna
            if(row):
                return True
            
            return False
            
        except Exception as e:
            print(e)

            return None

    @staticmethod
    # Función para verificar si un dispositivo es duplicado por su ip o mac
    def isDuplicateDevice(device_id, device_ip, device_mac):
        dbConnection = DBConnection()
        connection = dbConnection.getConnection()

        # SQL para verificar si un dispositivo es duplicado por su ip o mac
        sql = "SELECT * FROM devices WHERE NOT device_id = %s AND (device_ip = %s OR device_mac = %s)"

        row = None

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, (device_id, device_ip, device_mac))

                # Obtenemos el dispositivo por su ip o mac
                row = cursor.fetchone()

            dbConnection.closeConnection()

            # Si se obtuvo el dispositivo, se crea un objeto Device y se retorna
            if(row):
                return True
            
            return False
        
        except Exception as e:
            print(e)

            return None