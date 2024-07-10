#!/bin/bash

# Lane detection scriptini çalıştırma
echo "Lane detection scripti başlatılıyor..."
python lane_detection.py

# Pedestrian detection scriptini çalıştırma
echo "Pedestrian detection scripti başlatılıyor..."
python pedestrian_detection.py

# Stop sign detection scriptini çalıştırma
echo "Stop sign detection scripti başlatılıyor..."
python stop_sign_detection.py

# Traffic light detection scriptini çalıştırma
echo "Traffic light detection scripti başlatılıyor..."
python traffic_light_detection.py

# Vehicle detection scriptini çalıştırma
echo "Vehicle detection scripti başlatılıyor..."
python vehicle_detection.py

echo "Tüm scriptler başarıyla çalıştırıldı."
