from core.database import DBConnection
from models.device import Device

class DeviceCRUD:

    @staticmethod
    def create(device_ip, device_mac, device_status):
        dbConnection = DBConnection()
        connection = dbConnection.getConnection()

        sql = "INSERT INTO devices(device_ip, device_mac, device_status)values(%s,%s,%s) RETURNING device_id"

        row = None

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, (device_ip, device_mac, device_status))

                row = cursor.fetchone()

            connection.commit()
            dbConnection.closeConnection()

            return Device(row[0], device_ip, device_mac, device_status)

        except Exception as e:
            print(e)

            return None

    @staticmethod
    def getByID(device_id):
        dbConnection = DBConnection()
        connection = dbConnection.getConnection()

        sql = "SELECT * FROM devices WHERE device_id = %s"

        row = None

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, (str(device_id),))

                row = cursor.fetchone()

            dbConnection.closeConnection()

            if(row):
                return Device(row[0], row[1], row[2], row[3])
            
            return {}

        except Exception as e:
            print(e)

            return None

    @staticmethod
    def getByIP(device_ip):
        dbConnection = DBConnection()
        connection = dbConnection.getConnection()

        sql = "SELECT * FROM devices WHERE device_ip = %s"

        row = None

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, (device_ip,))
                
                row = cursor.fetchone()

            dbConnection.closeConnection()

            if(row):
                return Device(row[0], row[1], row[2], row[3])
            
            return {}
        
        except Exception as e:
            print(e)

            return None

    @staticmethod
    def getByMAC(device_mac):
        dbConnection = DBConnection()
        connection = dbConnection.getConnection()

        sql = "SELECT * FROM devices WHERE device_mac = %s"

        row = None

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, (device_mac,))

                row = cursor.fetchone()

            dbConnection.closeConnection()

            if(row):
                return Device(row[0], row[1], row[2], row[3])
            
            return {}

        except Exception as e:
            print(e)

            return None

    @staticmethod
    def getByStatus(device_status):
        dbConnection = DBConnection()
        connection = dbConnection.getConnection()

        sql = "SELECT * FROM devices WHERE device_status = %s"

        rows = None

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, (device_status,))
                
                rows = cursor.fetchall()

            dbConnection.closeConnection()

            devices = []

            for row in rows:
                devices += [Device(row[0], row[1], row[2], row[3])]

            return devices

        except Exception as e:
            print(e)

            return None

    @staticmethod
    def getAll():
        dbConnection = DBConnection()
        connection = dbConnection.getConnection()

        sql = "SELECT * FROM devices"

        rows = None

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)

                rows = cursor.fetchall()

            dbConnection.closeConnection()

            devices = []

            for row in rows:
                devices += [Device(row[0], row[1], row[2], row[3])]

            return devices

        except Exception as e:
            print(e)

            return None

    @staticmethod
    def updateByID(device_id, device_ip, device_mac, device_status):
        dbConnection = DBConnection()
        connection = dbConnection.getConnection()

        sql = "UPDATE devices SET device_ip = %s, device_mac = %s, device_status = %s WHERE device_id = %s"

        updated_rows = 0

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, (device_ip, device_mac, device_status, device_id))

                updated_rows = cursor.rowcount

            connection.commit()
            dbConnection.closeConnection()

            if(updated_rows > 0):
                return True

            return False

        except Exception as e:
            print(e)

            return None

    @staticmethod
    def deleteByID(device_id):
        dbConnection = DBConnection()
        connection = dbConnection.getConnection()

        sql = "DELETE FROM devices WHERE device_id = %s"

        deleted_rows = 0

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, (str(device_id),))

                deleted_rows = cursor.rowcount
                
            connection.commit()
            dbConnection.closeConnection()

            if(deleted_rows):
                return True
            
            return False

        except Exception as e:
            print(e)

            return None

    @staticmethod
    def deleteAll():
        dbConnection = DBConnection()
        connection = dbConnection.getConnection()

        sql = "DELETE FROM devices"

        deleted_rows = 0

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)

                deleted_rows = cursor.rowcount

            connection.commit()
            dbConnection.closeConnection()

            return deleted_rows

        except Exception as e:
            print(e)

            return None

    @staticmethod
    def countDevices():
        dbConnection = DBConnection()
        connection = dbConnection.getConnection()

        sql = "SELECT COUNT(*) FROM devices"

        rows_count = 0

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)

                rows_count = cursor.fetchone()[0]

            dbConnection.closeConnection()

            return rows_count
        
        except Exception as e:
            print(e)

            return None

    @staticmethod
    def deviceExists(device_ip, device_mac):
        dbConnection = DBConnection()
        connection = dbConnection.getConnection()

        sql = "SELECT * FROM devices WHERE device_ip = %s OR device_mac = %s"

        row = None

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, (device_ip, device_mac))

                row = cursor.fetchone()

            dbConnection.closeConnection()

            if(row):
                return True
            
            return False
            
        except Exception as e:
            print(e)

            return None

    @staticmethod
    def isDuplicateDevice(device_id, device_ip, device_mac):
        dbConnection = DBConnection()
        connection = dbConnection.getConnection()

        sql = "SELECT * FROM devices WHERE NOT device_id = %s AND (device_ip = %s OR device_mac = %s)"

        row = None

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, (device_id, device_ip, device_mac))

                row = cursor.fetchone()

            dbConnection.closeConnection()

            if(row):
                return True
            
            return False
        
        except Exception as e:
            print(e)

            return None