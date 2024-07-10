@echo off

REM Python yorumlayıcısının yolu
set PYTHON=python

REM Script dosyalarının adları
set SCRIPT1=lane_detection.py
set SCRIPT2=pedestrian_detection.py
set SCRIPT3=stop_sign_detection.py
set SCRIPT4=traffic_light_detection.py
set SCRIPT5=vehicle_detection.py

REM Her bir script dosyasını sırayla çalıştırma
%PYTHON% %SCRIPT1%
%PYTHON% %SCRIPT2%
%PYTHON% %SCRIPT3%
%PYTHON% %SCRIPT4%
%PYTHON% %SCRIPT5%

REM Çalışma tamamlandı mesajı
echo Tüm script dosyaları başarıyla çalıştırıldı.
pause
