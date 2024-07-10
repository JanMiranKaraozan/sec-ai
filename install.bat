#!/bin/bash

# Python yorumlayıcısının yolunu tanımla (eğer python3 gibi bir yorumlayıcı kullanıyorsanız)
PYTHON=python

# Pip'i güncelle
$PYTHON -m pip install --upgrade pip

# Gereken kütüphaneleri yükle
$PYTHON -m pip install opencv-python
$PYTHON -m pip install numpy

# Kütüphanelerin başarıyla yüklendiğini belirten mesajı yazdır
echo "Pip güncellendi, OpenCV ve NumPy kütüphaneleri başarıyla yüklendi."
