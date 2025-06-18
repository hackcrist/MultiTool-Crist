# 💻 Crist MultiTool

Herramienta de hacking ético profesional para Termux y Kali Linux.  
Incluye escaneo profundo de red, análisis de puertos abiertos, detección de IP, descarga de videos y efectos visuales estilo hacker.

---

![Portada](imagen.png)

---

## 🚀 Funciones principales

✅ Escaneo de red completo con puertos y versiones  
✅ Visualización de IP local y pública  
✅ Descarga de videos desde múltiples plataformas con `yt-dlp`  
✅ Diagnóstico total en un clic  
✅ Efectos visuales (banner, cuenta regresiva, Matrix style)  
✅ Compatible con Termux y Kali Linux  
✅ Instalación como paquete `.deb` en sistemas Debian

---

## 📦 Instalación en Termux

### 🔧 Requisitos previos

```bash
pkg update -y && pkg upgrade -y
```

```bash
pkg install git python figlet lolcat -y
```

```bash
pip install colorama pyfiglet
```

```bash
pkg install nmap -y
```

```bash
pkg install iproute2 -y
```

---

### 📥 Clonación e instalación

```bash
git clone https://github.com/hackcrist/MultiTool-Crist.git
```

```bash
cd MultiTool-Crist
```

```bash
bash install.sh
```

---

### ▶️ Ejecutar herramienta

```bash
crist-multitool
```

---

## 🐧 Instalación en Kali Linux / Debian

### 📥 Descargar e instalar el paquete `.deb`

```bash
wget https://chat.openai.com/sandbox/download/crist-multitool_1.0_all.deb
```

```bash
sudo dpkg -i crist-multitool_1.0_all.deb
```

```bash
crist-multitool
```

---

## 🛠️ Requisitos

- Python 3  
- figlet + lolcat (efectos visuales)  
- yt-dlp (para descarga de videos)  
- nmap (para escaneo de red)  
- curl (para obtener IP pública)

---

## 🧠 Autor

**Hackcrist**  
⭐ Si te gusta este proyecto, ¡dale una estrella en GitHub!  
💸 Donaciones: `miniosjuan89@gmail.com` (PayPal)

---

## 🛡️ Uso ético

Esta herramienta está diseñada únicamente para pruebas de seguridad autorizadas y propósitos educativos.  
**No la uses para fines ilegales.**
