@echo off

REM Python yorumlayıcısının yolu
set PYTHON=python

REM Gereken kütüphaneleri yüklemek için pip komutları
%PYTHON% -m pip install opencv-python
%PYTHON% -m pip install numpy

REM Kütüphanelerin başarıyla yüklendiğini belirten mesaj
echo OpenCV ve NumPy kutuphaneleri basariyla yuklendi. Herhangi bir tusa basarak cikin.
pause
