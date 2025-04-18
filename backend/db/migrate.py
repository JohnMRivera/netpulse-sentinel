from db.migrations import CreateUsers
from db.migrations import CreateRoles
from db.migrations import CreatePermissions
from db.migrations import CreateModules
from db.migrations import CreateDevices
from db.migrations import CreateDevicesLogs
from db.migrations import CreateAlerts
from db.migrations import CreateUsersDevicesAlerts
from db.migrations import CreateAlertsLogs
import os
import sys

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