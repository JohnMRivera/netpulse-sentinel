# NetPulse-Sentinel

NetPulse-Sentinel es un sistema de monitoreo de red con generación de alertas en tiempo real. Permite supervisar dispositivos en una red (routers, switches, servidores, etc.), detectando fallos y notificando a los administradores. Se compone de un backend en Python, un frontend en Vue.js y scripts en Bash y Batch para la automatización en Linux y Windows.

## Características principales
- **Monitoreo de dispositivos en red** mediante pings y análisis de conexiones.
- **Interfaz gráfica en Vue.js** para visualizar el estado de los dispositivos.
- **Notificaciones en tiempo real** usando WebSockets o AJAX.
- **Sistema de alertas** vía correo electrónico o Telegram.
- **Compatibilidad multiplataforma** (Linux y Windows).

## Tecnologías utilizadas
- **Backend**: Python (Flask)
- **Frontend**: Vue.js
- **Automatización**: Bash (Linux) y Batch (Windows)
- **Base de datos**: PostgreSQL
- **Comunicación en tiempo real**: WebSockets / AJAX

## Instalación y ejecución

### Requisitos previos
- Python 3
- Node.js y npm
- PostgreSQL
- Git

### Clonar el repositorio
```bash
git clone https://github.com/JohnMRivera/netpulse-sentinel.git
cd netpulse-sentinel
```

### Configurar y ejecutar el backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # En Windows usar 'venv\Scripts\activate' para activar el entorno virtual
pip install -r requirements.txt
python main.py
```

### Configurar y ejecutar el frontend
```bash
cd frontend
npm install
npm run dev
```

### Ejecutar el sistema completo
```bash
./start.sh  # En Linux
start.bat   # En Windows
```

### **Autores**
- Juan Manuel Rivera Olvera