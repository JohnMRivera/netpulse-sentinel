from flask import Blueprint, jsonify, request
from crud.device import DeviceCRUD
from models.device import Device

device_bp = Blueprint("devices", __name__)

@device_bp.route("/", methods=["POST"])
def create():
    try:
        data = request.json

        if not data:
            return jsonify({
                "error": "No se recibieron datos"
            }), 400

        device_ip = data["device_ip"]
        device_mac = data["device_mac"]
        device_status = data["device_status"]

        if not device_ip or not device_mac or not device_status:
            return jsonify({
                "error": "Faltan datos"
            }), 400
        
        device_exists = DeviceCRUD.deviceExists(device_ip, device_mac)

        if device_exists is None:
            return jsonify({
                "message": "Error al comprobar dispositivo existente"
            }), 409

        elif device_exists:
            return jsonify({
                "message": "El dispositivo ya existe"
            }), 409

        device = DeviceCRUD.create(device_ip, device_mac, device_status)
        
        if device is None:
            return jsonify({
                "error": "Error al intentar registrar el dispositivo"
            }), 400

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
    
@device_bp.route("/<int:device_id>", methods=["GET"])
def getByID(device_id):
    try:
        device = DeviceCRUD.getByID(device_id)

        if device is None:
            return jsonify({
                "error": "Error al obtener el dispositivo",
            }), 400
    
        if not device:
            return jsonify({
                "error": "Dispositivo no encontrado",
            }), 404

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

@device_bp.route("/ip/<string:device_ip>", methods=["GET"])
def getByIP(device_ip):
    try:
        if not device_ip:
            return jsonify({
                "error": "Faltan datos"
            }), 400
        
        device = DeviceCRUD.getByIP(device_ip)

        if device is None:
            return jsonify({
                "error": "Error al obtener el dispositivo",
            }), 400
    
        if not device:
            return jsonify({
                "error": "Dispositivo no encontrado",
            }), 404

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

@device_bp.route("/mac/<string:device_mac>", methods=["GET"])
def getByMAC(device_mac):
    try:
        if not device_mac:
            return jsonify({
                "error": "Faltan datos"
            }), 400
        
        device = DeviceCRUD.getByMAC(device_mac)
        
        if device is None:
            return jsonify({
                "error": "Error al obtener el dispositivo",
            }), 400
    
        if not device:
            return jsonify({
                "error": "Dispositivo no encontrado",
            }), 404

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

@device_bp.route("/status/<string:device_status>", methods=["GET"])
def getByStatus(device_status):
    try:
        if not device_status:
            return jsonify({
                "error": "Faltan datos"
            }), 400
        
        devices = DeviceCRUD.getByStatus(device_status)

        print(devices)

        if devices is None:
            return jsonify({
                "error": "Error al obtener los dispositivos"
            }), 400

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

@device_bp.route("/", methods=["GET"])
def getAll():
    try:
        devices = DeviceCRUD.getAll()

        if devices is None:
            return jsonify({
                "error": "Error al obtener dispositivos"
            }), 400

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
    
@device_bp.route("/<int:device_id>", methods=["PUT"])
def update(device_id):
    try:
        data = request.json

        if not data:
            return jsonify({
                "error": "No se recibieron datos",
                "data": data
            }), 400

        device_ip = data["device_ip"]
        device_mac = data["device_mac"]
        device_status = data["device_status"]

        if not device_ip or not device_mac or not device_status:
            return jsonify({
                "error": "Faltan datos"
            })
        
        device_exists = DeviceCRUD.isDuplicateDevice(device_id, device_ip, device_mac)

        if device_exists is None:
            return jsonify({
                "error": "Error al comprobar dispositivo duplicado"
            }), 400

        elif device_exists:
            return jsonify({
                "error": "La IP y dirección MAC ya existen"
            }), 409
        
        status = DeviceCRUD.updateByID(device_id, device_ip, device_mac, device_status)

        if status is None:
            return jsonify({
                "error": "Error al intentar actualizar el dispositivo"
            }), 400

        if not status:
            return jsonify({
                "error": "Dispositivo no actualizable"
            }), 404

        return jsonify({
            "message": "Dispositivo actualizado exitosamente",
        }), 201
        
    except Exception as e:
        return jsonify({
            "message": f"Error interno del servidor"
        }), 500

@device_bp.route("/<int:device_id>", methods=["DELETE"])
def delete(device_id):
    try:
        if not device_id:
            return jsonify({
                "error": "Faltan parametros"
            }), 400

        status = DeviceCRUD.deleteByID(device_id)

        if status is None:
            return jsonify({
                "error": "Error al intentar eliminar el dispositivo"
            }), 400

        if not status:
            return jsonify({
                "error": "Dispositivo no eliminable"
            }), 404
        
        return jsonify({
            "message": "Dispositivo eliminado exitosamente"
        }), 201

    except Exception as e:
        return jsonify({
            "error": "Error interno del servidor"
        }), 500
    
@device_bp.route("/", methods=["DELETE"])
def deleteAll():
    try:
        deleted_rows = DeviceCRUD.deleteAll()

        if deleted_rows is None:
            return jsonify({
                "error": "Error al intentar eliminar los dispositivos"
            }), 400

        return jsonify({
            "message": f"Se eliminaron {deleted_rows} dispositivos exitosamente"
        }), 200
        
    except Exception as e:
        return jsonify({
            "error": "Error interno del servidor"
        }), 500

@device_bp.route("/count/", methods=["GET"])
def countDevices():
    try:
        count_devices = DeviceCRUD.countDevices()

        if count_devices is None:
            return jsonify({
                "error": "Error al intentar obtener la cantidad de dispositivos"
            }), 400

        return jsonify({
            "count_devices": count_devices
        }), 200

    except Exception as e:
        return jsonify({
            "error": f"Error interno del servidor: {str(e)}"
        }), 500
