#!/usr/bin/env python3
import os
import subprocess
from time import sleep
from pyfiglet import Figlet
from colorama import Fore, init

init(autoreset=True)

def banner():
    os.system("clear")
    fig = Figlet(font='slant')
    print(Fore.GREEN + fig.renderText("Crist MultiTool"))
    print(Fore.CYAN + "🧠 Herramienta multifuncional para Termux y Kali Linux")
    print(Fore.YELLOW + "By Crist Hack – Solo para uso ético\n")

def escanear_red():
    red = input(Fore.CYAN + "🔍 Ingresa el rango de red (ej. 192.168.1.0/24): ")
    subprocess.run(["nmap", "-sn", red])

def ver_ip():
    print(Fore.YELLOW + "\n🌐 IP pública:")
    subprocess.run("curl -s ifconfig.me", shell=True)
    print(Fore.YELLOW + "\n📡 IP local:")
    subprocess.run("ip a | grep inet", shell=True)

def descargar_video():
    url = input(Fore.CYAN + "📥 Ingresa la URL del video: ")
    subprocess.run(["yt-dlp", url])

def diagnostico_total():
    ver_ip()
    sleep(1)
    escanear_red()

def menu():
    while True:
        banner()
        print(Fore.MAGENTA + "1) Escanear red local")
        print("   2) Ver IP local y pública")
        print("   3) Descargar videos")
        print("   4) Modo diagnóstico total")
        print("   5) Salir")
        print(Fore.YELLOW + "\n⭐ Si te gusta, deja una estrella en GitHub")
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
     
