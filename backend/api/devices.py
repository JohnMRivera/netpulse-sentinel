from flask import Blueprint, jsonify, request
from crud.devices import DevicesCRUD
from models.device import Device

# Definición del blueprint `devices_bp` que responde a solicitudes en la raíz ("/").
devices_bp = Blueprint("devices", __name__)

# Ruta para crear un nuevo dispositivo.
@devices_bp.route("/", methods=["POST"])
# Función para crear un nuevo dispositivo.
def create():
    try:
        # Obtener los datos de la solicitud JSON.
        data = request.json

        # Verificar si se recibieron datos.
        if not data:
            return jsonify({
                "error": "No se recibieron datos"
            }), 400

        device_ip = data["device_ip"]
        device_mac = data["device_mac"]
        device_status = data["device_status"]

        # Verificar si faltan datos.
        if not device_ip or not device_mac or not device_status:
            return jsonify({
                "error": "Faltan datos"
            }), 400
        
        # Comprobar si el dispositivo ya existe en la base de datos.
        device_exists = DevicesCRUD.deviceExists(device_ip, device_mac)

        # Si ocurre un error al comprobar la existencia del dispositivo, devolver un error.
        if device_exists is None:
            return jsonify({
                "message": "Error al comprobar dispositivo existente"
            }), 409

        # Si el dispositivo ya existe, devolver un mensaje de conflicto.
        elif device_exists:
            return jsonify({
                "message": "El dispositivo ya existe"
            }), 409

        # Crear un nuevo dispositivo en la base de datos.
        device = DevicesCRUD.create(device_ip, device_mac, device_status)
        
        # Si ocurre un error al crear el dispositivo, devolver un error.
        if device is None:
            return jsonify({
                "error": "Error al intentar registrar el dispositivo"
            }), 400

        # Devolver respuesta exitosa con los datos del dispositivo creado.
        return jsonify({
            "message": "Dispositivo registrado exitosamente",
            "data": {
                "device_id": device.device_id,
                "device_ip": device.device_ip,
                "device_mac": device.device_mac,
                "device_status": device.device_status
            }
        }), 201
            
    except Exception as e:
        return jsonify({
            "error": f"Error interno del servidor: {str(e)}"
        }), 500
    
# Ruta para obtener un dispositivo por su ID.
@devices_bp.route("/<int:device_id>", methods=["GET"])
# Función para obtener un dispositivo por su ID.
def getByID(device_id):
    try:
        # Verificar si se proporcionó un ID de dispositivo.
        device = DevicesCRUD.getByID(device_id)

        # Si ocurre un error al obtener el dispositivo, devolver un error.
        if device is None:
            return jsonify({
                "error": "Error al obtener el dispositivo",
            }), 400
    
        # Si no se encuentra el dispositivo, devolver un error.
        if not device:
            return jsonify({
                "error": "Dispositivo no encontrado",
            }), 404

        # Devolver respuesta exitosa con los datos del dispositivo.
        return jsonify({
            "device_id": device.device_id,
            "device_ip": device.device_ip,
            "device_mac": device.device_mac,
            "device_status": device.device_status
        }), 200
        
    except Exception as e:
        return jsonify({
            "error": f"Error interno del servidor: {str(e)}"
        }), 500

# Ruta para obtener un dispositivo por su dirección IP.
@devices_bp.route("/ip/<string:device_ip>", methods=["GET"])
# Función para obtener un dispositivo por su dirección IP.
def getByIP(device_ip):
    try:
        # Verificar si se proporcionó una dirección IP.
        if not device_ip:
            return jsonify({
                "error": "Faltan datos"
            }), 400
        
        # Obtener el dispositivo por su dirección IP.
        device = DevicesCRUD.getByIP(device_ip)

        # Si ocurre un error al obtener el dispositivo, devolver un error.
        if device is None:
            return jsonify({
                "error": "Error al obtener el dispositivo",
            }), 400
    
        # Si no se encuentra el dispositivo, devolver un error.
        if not device:
            return jsonify({
                "error": "Dispositivo no encontrado",
            }), 404

        # Devolver respuesta exitosa con los datos del dispositivo.
        return jsonify({
            "device_id": device.device_id,
            "device_ip": device.device_ip,
            "device_mac": device.device_mac,
            "device_status": device.device_status
        }), 200
        
    except Exception as e:
        return jsonify({
            "error": f"Error interno del servidor: {str(e)}"
        }), 500

# Ruta para obtener un dispositivo por su dirección MAC.
@devices_bp.route("/mac/<string:device_mac>", methods=["GET"])
# Función para obtener un dispositivo por su dirección MAC.
def getByMAC(device_mac):
    try:
        # Verificar si se proporcionó una dirección MAC.
        if not device_mac:
            return jsonify({
                "error": "Faltan datos"
            }), 400
        
        # Obtener el dispositivo por su dirección MAC.
        device = DevicesCRUD.getByMAC(device_mac)
        
        # Si ocurre un error al obtener el dispositivo, devolver un error.
        if device is None:
            return jsonify({
                "error": "Error al obtener el dispositivo",
            }), 400
    
        # Si no se encuentra el dispositivo, devolver un error.
        if not device:
            return jsonify({
                "error": "Dispositivo no encontrado",
            }), 404

        # Devolver respuesta exitosa con los datos del dispositivo.
        return jsonify({
            "device_id": device.device_id,
            "device_ip": device.device_ip,
            "device_mac": device.device_mac,
            "device_status": device.device_status
        }), 200
        
    except Exception as e:
        return jsonify({
            "error": f"Error interno del servidor: {str(e)}"
        }), 500

# Ruta para obtener dispositivos por su estado.
@devices_bp.route("/status/<string:device_status>", methods=["GET"])
# Función para obtener dispositivos por su estado.
def getByStatus(device_status):
    try:
        # Verificar si se proporcionó un estado de dispositivo.
        if not device_status:
            return jsonify({
                "error": "Faltan datos"
            }), 400
        
        # Obtener dispositivos por su estado.
        devices = DevicesCRUD.getByStatus(device_status)

        # Si ocurre un error al obtener los dispositivos, devolver un error.
        if devices is None:
            return jsonify({
                "error": "Error al obtener los dispositivos"
            }), 400

        # Si no se encuentran dispositivos, devolver un error.
        return jsonify([{
            "device_id": device.device_id,
            "device_ip": device.device_ip,
            "device_mac": device.device_mac,
            "device_status": device.device_status
        } for device in devices]), 200
    
    except Exception as e:
        return jsonify({
            "error": f"Error interno del servidor: {str(e)}"
        })

# Ruta para obtener todos los dispositivos.
@devices_bp.route("/", methods=["GET"])
# Función para obtener todos los dispositivos.
def getAll():
    try:
        # Obtener todos los dispositivos.
        devices = DevicesCRUD.getAll()

        # Si ocurre un error al obtener los dispositivos, devolver un error.
        if devices is None:
            return jsonify({
                "error": "Error al obtener dispositivos"
            }), 400

        # Si no se encuentran dispositivos, devolver un error.
        return jsonify([{
            "device_id": device.device_id,
            "device_ip": device.device_ip,
            "device_mac": device.device_mac,
            "device_status": device.device_status
        } for device in devices]), 200
        
    except Exception as e:
        return jsonify({
            "error": f"Error interno del servidor: {str(e)}"
        }), 500
    
# Ruta para actualizar un dispositivo por su ID.
@devices_bp.route("/<int:device_id>", methods=["PUT"])
# Función para actualizar un dispositivo por su ID.
def update(device_id):
    try:
        # Verificar si se proporcionó un ID de dispositivo.
        data = request.json

        # Obtener los datos de la solicitud JSON.
        if not data:
            return jsonify({
                "error": "No se recibieron datos",
                "data": data
            }), 400

        device_ip = data["device_ip"]
        device_mac = data["device_mac"]
        device_status = data["device_status"]

        # Verificar si faltan datos.
        if not device_ip or not device_mac or not device_status:
            return jsonify({
                "error": "Faltan datos"
            })
        
        # Comprobar si el dispositivo ya existe en la base de datos.
        device_exists = DevicesCRUD.isDuplicateDevice(device_id, device_ip, device_mac)

        # Si ocurre un error al comprobar la existencia del dispositivo, devolver un error.
        if device_exists is None:
            return jsonify({
                "error": "Error al comprobar dispositivo duplicado"
            }), 400

        # Si el dispositivo ya existe, devolver un mensaje de conflicto.
        elif device_exists:
            return jsonify({
                "error": "La IP y dirección MAC ya existen"
            }), 409
        
        # Actualizar el dispositivo en la base de datos.
        device = DevicesCRUD.updateByID(device_id, device_ip, device_mac, device_status)

        # Si ocurre un error al actualizar el dispositivo, devolver un error.
        if device is None:
            return jsonify({
                "error": "Error al intentar actualizar el dispositivo"
            }), 400

        # Si no se encuentra el dispositivo, devolver un error.
        if not device:
            return jsonify({
                "error": "Dispositivo no actualizable"
            }), 404

        # Devolver respuesta exitosa con los datos del dispositivo actualizado.
        return jsonify({
            "message": "Dispositivo actualizado exitosamente",
            "data": {
                "device_id": device.device_id,
                "device_ip": device.device_ip,
                "device_mac": device.device_mac,
                "device_status": device.device_status
            }
        }), 201
        
    except Exception as e:
        return jsonify({
            "message": f"Error interno del servidor: {str(e)}"
        }), 500

# Ruta para eliminar un dispositivo por su ID.
@devices_bp.route("/<int:device_id>", methods=["DELETE"])
# Función para eliminar un dispositivo por su ID.
def delete(device_id):
    try:
        # Verificar si se proporcionó un ID de dispositivo.
        if not device_id:
            return jsonify({
                "error": "Faltan parametros"
            }), 400

        # Comprobar si el dispositivo existe en la base de datos.
        status = DevicesCRUD.deleteByID(device_id)

        # Si ocurre un error al comprobar la existencia del dispositivo, devolver un error.
        if status is None:
            return jsonify({
                "error": "Error al intentar eliminar el dispositivo"
            }), 400

        # Si no se encuentra el dispositivo, devolver un error.
        if not status:
            return jsonify({
                "error": "Dispositivo no eliminable"
            }), 404
        
        # Devolver respuesta exitosa con un mensaje de eliminación.
        return jsonify({
            "message": "Dispositivo eliminado exitosamente"
        }), 201

    except Exception as e:
        return jsonify({
            "error": f"Error interno del servidor: {str(e)}"
        }), 500
    
@devices_bp.route("/", methods=["DELETE"])
def deleteAll():
    try:
        # Eliminar todos los dispositivos de la base de datos.
        deleted_rows = DevicesCRUD.deleteAll()

        # Si ocurre un error al eliminar los dispositivos, devolver un error.
        if deleted_rows is None:
            return jsonify({
                "error": "Error al intentar eliminar los dispositivos"
            }), 400

        # Si no se encuentran dispositivos, devolver un error.
        return jsonify({
            "message": f"Se eliminaron {deleted_rows} dispositivos exitosamente"
        }), 200
        
    except Exception as e:
        return jsonify({
            "error": f"Error interno del servidor: {str(e)}"
        }), 500

@devices_bp.route("/count/", methods=["GET"])
def countDevices():
    try:
        # Obtener la cantidad de dispositivos en la base de datos.
        count_devices = DevicesCRUD.countDevices()

        # Si ocurre un error al contar los dispositivos, devolver un error.
        if count_devices is None:
            return jsonify({
                "error": "Error al intentar obtener la cantidad de dispositivos"
            }), 400

        # Si no se encuentran dispositivos, devolver un error.
        return jsonify({
            "count_devices": count_devices
        }), 200

    except Exception as e:
        return jsonify({
            "error": f"Error interno del servidor: {str(e)}"
        }), 500
