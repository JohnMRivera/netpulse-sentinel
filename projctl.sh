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

case $1 in
    --start | -s)
        # Verificando que los archivos .pid existan
        if [ ! -f backend.pid ] && [ ! -f fronted.pid ] && [ ! -f electron.pid ]; then
            echo "Iniciando proyecto..."

            # Iniciando Backend
            source backend/venv/bin/activate
            python backend/main.py & echo $! > backend.pid

            # Iniciando Frontend
            cd frontend
            npm run dev & echo $! > ../frontend.pid

            # Iniciando Electorn
            npm run electron:start & echo $! > ../electron.pid
            ..

            echo "Proyecto iniciado correctamente."
        else
            echo "El proyecto ya se encuentra en ejecución."
        fi
    ;;
    --end | -e)
        echo "Finzalizando el proyecto..."
        # Llamando a la función end_process
        end_process "backend.pid"
        end_process "frontend.pid"
        end_process "electron.pid"
        echo "Proyecto frinalizado."
    ;;
    --help | -h)
        echo -e "Uso: projctl.sh [opción]\n"
        echo "  --start, -s   Inicia el proyecto."
        echo "  --end, -e     Detiene el proyecto."
        echo "  --help, -h    Muestra este mensaje de ayuda."
        echo ""
    ;;
    *)
        echo "Opción no valida\nUsa 'projctl.sh --help' para más información."
    ;;
esac