#!/bin/bash

# Colores
verde="\033[1;32m"
reset="\033[0m"

# Función: Banner inicial
function banner_inicio() {
    clear
    echo -e "${verde}"
    figlet "Crist MultiTool" | lolcat
    echo -e "${reset}"
    echo -e "${verde}🚀 Iniciando instalación...${reset}"
    sleep 1
}

# Función: Cuenta regresiva
function cuenta_regresiva() {
    echo -e "\n${verde}Comenzando en...${reset}"
    for i in 3 2 1; do
        echo -e "${verde}$i...${reset}"
        sleep 1
    done
}

# Función: Simulación tipo Matrix
function simulacion_matrix() {
    echo -e "\n${verde}Cargando módulos secretos...${reset}"
    sleep 1
    for i in {1..20}; do
        echo "$RANDOM $RANDOM $RANDOM $RANDOM $RANDOM" | md5sum | cut -c1-50 | lolcat
        sleep 0.05
    done
}

# Función: Instalación real
function instalar() {
    echo -e "\n${verde}📦 Copiando archivos...${reset}"
    cp crist_multitool.py /data/data/com.termux/files/usr/bin/crist-multitool
    chmod +x /data/data/com.termux/files/usr/bin/crist-multitool
    echo -e "${verde}✅ Instalación completada. Ejecuta: crist-multitool${reset}"
}

# Ejecutar todo
banner_inicio
cuenta_regresiva
simulacion_matrix
instalar
