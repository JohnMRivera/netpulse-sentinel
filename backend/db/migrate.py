import psycopg2
import dotenv
import os

from core import DBConnection
from db.migrations import CreateUsers
from db.migrations import CreateRoles
from db.migrations import CreatePermissions
from db.migrations import CreateModules
from db.migrations import CreateDevices
from db.migrations import CreateDevicesLogs
from db.migrations import CreateAlerts
from db.migrations import CreateUsersDevicesAlerts
from db.migrations import CreateAlertsLogs

dbConnection = DBConnection()
connection = dbConnection.getConnection()

dotenv.load_dotenv()
DB_NAME = os.getenv('DB_NAME')

def createDB():
    sql = "SELECT 1 FROM pg_database WHERE datname = %s;"

    rowcount = None

    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, (DB_NAME,))

            rowcount = cursor.rowcount

        if rowcount == 0:
            print(f"La base de datos {DB_NAME} no existe\nCreando base de datos...")

            sql = f"CREATE DATABASE {DB_NAME}"

            try:
                with connection.cursor() as cursor:
                    cursor.execute(sql)

                    print(f"Base de datos {DB_NAME} creada exitosamente")
            except psycopg2.Error as e:
                print(f"Error al intentar crear la base de datos")

    except psycopg2.Error as e:
        print(f"Error al intentar varificar la base de datos: {str(e)}")

createDB()

create_devices = CreateDevices()
create_devices.up()

create_users = CreateUsers()
create_users.up()

create_roles = CreateRoles()
create_roles.up()

create_permissions = CreatePermissions()
create_permissions.up()

create_modules = CreateModules()
create_modules.up()

create_devices_logs = CreateDevicesLogs()
create_devices_logs.up()

create_alerts = CreateAlerts()
create_alerts.up()

create_uda = CreateUsersDevicesAlerts()
create_uda.up()

create_alerts_logs = CreateAlertsLogs()
create_alerts_logs.up()