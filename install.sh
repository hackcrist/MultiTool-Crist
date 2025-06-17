#!/bin/bash
chmod +x crist_multitool.py
cp crist_multitool.py /data/data/com.termux/files/usr/bin/crist-multitool 2>/dev/null || sudo cp crist_multitool.py /usr/local/bin/crist-multitool
echo "✅ Instalación completada. Ejecuta con: crist-multitool"
