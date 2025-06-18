#!/usr/bin/env python3
import os
import subprocess
import shutil
from time import sleep
from pyfiglet import Figlet
from colorama import Fore, init

init(autoreset=True)

def verificar_dependencias():
    if not shutil.which("nmap"):
        print(Fore.YELLOW + "🔧 Instalando nmap...")
        subprocess.run("pkg install nmap -y", shell=True)
    if not shutil.which("curl"):
        print(Fore.YELLOW + "🔧 Instalando curl...")
        subprocess.run("pkg install curl -y", shell=True)
    if not shutil.which("ifconfig"):
        print(Fore.YELLOW + "🔧 Instalando net-tools...")
        subprocess.run("pkg install net-tools -y", shell=True)

def banner():
    os.system("clear")
    fig = Figlet(font='slant')
    print(Fore.GREEN + fig.renderText("Crist MultiTool"))
    print(Fore.CYAN + "🧠 Herramienta multifuncional para Termux y Kali Linux")
    print(Fore.YELLOW + "By Crist Hack – Solo para uso ético\n")

def escanear_red():
    red = input(Fore.CYAN + "🔍 Ingresa IP o rango (ej. 192.168.1.1 o 192.168.1.0/24): ")
    print(Fore.YELLOW + "\n🔎 Escaneando puertos abiertos y servicios...
")
    subprocess.run(f"nmap -sV -T4 -Pn -p- {red}", shell=True)

def ver_ip():
    print(Fore.YELLOW + "\n🌐 IP pública:")
    subprocess.run("curl -s ifconfig.me", shell=True)
    print(Fore.YELLOW + "\n📡 IP local:")
    subprocess.run("ifconfig", shell=True)

def descargar_video():
    url = input(Fore.CYAN + "📥 Ingresa la URL del video: ")
    print(Fore.YELLOW + "\n⏬ Descargando con yt-dlp...
")
    subprocess.run(["yt-dlp", url])

def diagnostico_total():
    print(Fore.CYAN + "\n🔧 Iniciando diagnóstico total...
")
    ver_ip()
    sleep(1)
    escanear_red()

def menu():
    verificar_dependencias()
    while True:
        banner()
        print(Fore.MAGENTA + "1) Escanear red con puertos")
        print("   2) Ver IP local y pública")
        print("   3) Descargar videos (yt-dlp)")
        print("   4) Modo diagnóstico total")
        print("   5) Salir")
        print(Fore.YELLOW + "\n⭐ Si te gusta, deja una estrella en GitHub")
        print("💸 Donaciones: miniosjuan89@gmail.com (PayPal)\n")
        opcion = input(Fore.GREEN + "👉 Opción: ")

        if opcion == "1":
            escanear_red()
        elif opcion == "2":
            ver_ip()
        elif opcion == "3":
            descargar_video()
        elif opcion == "4":
            diagnostico_total()
        elif opcion == "5":
            print(Fore.RED + "👋 Saliendo...")
            break
        else:
            print(Fore.RED + "❌ Opción inválida")
        input(Fore.CYAN + "\nPresiona ENTER para continuar...")

menu()
