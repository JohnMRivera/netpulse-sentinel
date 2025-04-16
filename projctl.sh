#!/bin/bash

# Función para eliminar procesos por PID del archivo .pid
function end_process(){
    local NAME_FILE=$1

    # Verificando que el archivo exista
    if [ -f $1 ]; then
        PID=$(cat $NAME_FILE)
        
        # Verificar que el proceso exista
        if ps -p $PID &> /dev/null; then
            echo "Finalizando proceso: $(ps -p $PID -o cmd=) (PID: $PID)"
            # Deteniendo el proceso por PID y sus procesos hijos
            kill -9 $(pstree -T -p $PID | grep -oE "\([0-9]+\)" | tr -d "()")
            echo "Proceso con pid $PID terminado exitosamente"
        else
            echo "El proceso con pid $PID no existe."
        fi

        # Eliminando archivo .pid
        rm $NAME_FILE
    else
        echo "No se encontró el archivo $NAME_FILE."
    fi
}

NPS_PATH=$(cd $(dirname $0) && pwd)
cd $NPS_PATH

case $1 in
    --run | -r)
        # Verificando que los archivos .pid existan
        if [ ! -f backend.pid ] && [ ! -f fronted.pid ] && [ ! -f electron.pid ]; then
            echo "Iniciando proyecto..."

            # Iniciando Backend
            source backend/venv/bin/activate
            python backend/main.py & echo $! > backend.pid

            # Iniciando Frontend
            cd frontend
            npm run dev & echo $! > ../frontend.pid

            # Dormir el proceso para cargar vite antes de cargar electron
            until curl -s "http://$FRONTEND_HOST:$FRONTEND_PORT" > /dev/null; do
                sleep 0.5
            done
            
            # Iniciando Electron
            npm run electron:start & echo $! > ../electron.pid
            ..

            sleep 3

            echo "Backend corriendo en $BACKEND_HOST:$BACKEND_PORT"
            echo "Frontend corriendo en $FRONTEND_HOST:$FRONTEND_PORT"

            echo "Proyecto iniciado correctamente."
        else
            echo "El proyecto ya se encuentra en ejecución."
        fi
    ;;
    --stop | -s)
        echo "Finalizando el proyecto..."
        # Llamando a la función end_process
        end_process "backend.pid"
        end_process "frontend.pid"
        end_process "electron.pid"
        echo "Proyecto frinalizado."
    ;;
    --export-env | -e)
            # Verificar que el fichero .env exista
            if [[ -f .env ]]; then
                # Exportando variables de entorno de .env
                # export $(grep -v "^#" .env | xargs)
                sed -i "s|^NPS_PATH=.*|NPS_PATH=$NPS_PATH|" ".env"
                source .env
            else
                echo "No existe el fichero .env\nPuede crearlo manualmente y definir las variables de entorno"
            fi
    ;;
    --help | -h)
        export $(grep -v "^#" .env | xargs)
        echo -e "Uso: projctl.sh [opción]\n"
        echo "  --run, -r           Inicia el proyecto."
        echo "  --stop, -s          Detiene el proyecto."
        echo "  --help, -h          Muestra este mensaje de ayuda."
        echo "  --export-env, -e    Exportar variables de entorno del archivo .env"
    ;;
    *)
        echo "Opción no valida\nUsa 'projctl.sh --help' para más información."
    ;;
esac