![SEC AI](repo/image.png)

# SEC AI
- Save Envinronment Car LLC © için SEC AI® resmi kod deposudur.
- Bu Yazılım GNU Affero Kamu Lisansı 3.0 altında dağıtılmaktadır.
- Veriler ve veritabanları SEC OpenData Lisansı 1.0 altında dağıtılmaktadır.

#### Model 0.1 Özellikleri

- OpenCV ve Python 3 kullanarak aşağıdakileri yapma kapasitesine sahiptir.

1. Trafik ışıklarını ve ışıkların durumunu algılar ve tanımlar
2. Yol üzerindeki trafik şeritlerini algılar ve takip eder.
3. Yayaları algılar ve takip eder.
4. Dur levhalarını algılar ve tanımlar.
5. Araçları algılar ve tanımlar.

NOT: Model 0.1 OpenCV kullanılarak geliştirilmiştir. OpenCV kullanımı bir üst model itibari ile kaldırılmıştır. Model 0.1 Linux ve Windows ile uyumlu geliştirilmektedir. Bir üst model itibari ile Windows uyumluluk geliştirilmeleri yapılmayacaktır.

#### Gelecek Model 1.0 özellikleri

- TensorFlow Lite ve Python 3 kullanarak aşağıdakileri yapma kapasitesine sahiptir.

1. Türkiyede kullanımda olan tüm trafik levhalarını algılar.
2. Türkiyede kullanımda olan tüm işaretlerini algılar.
3. Veritabanında kayıtlı olan araçları algılar, takip edebilir ve durumlarını analiz edebilir.
4. Yayaları algılar ve durumlarını takip edebilir.

## İnşa etme, Geliştirme ve Dağıtma

### Gerekliliklerin kurulması (Windows)
install.bat dosyasını yönetici olarak çalıştırınız. Gerekli tüm gereklilikler otomatik olarak kurulacaktır.

### Gerekliliklerin kurulması (GNU Linux Debian Dağıtımları)
Aşağıdaki gereklilikleri kurunuz. 

    python -m pip install opencv-python
    python -m pip install numpy
    
Bir sanal ortam oluşturmanız gerekebilir

    python -m venv sec-ai-env
    
### Windows için başlatma
main.bat dosyasını çalıştırınız.

### Linux için başlatma.
main.sh dosyasını aşağıdaki gibi çalıştırınız.

    chmod +x main.sh
    ./main.sh

## Katkı sunma

Yazılımın ve veritabanının geliştirilmesinde katkıda bulunan herkesin ismi ve mottosu kod deposunda sonsuza dek yayınlanacaktır. Buna yazılım ve veritabanına dahil edilen çatallamalarda dahildir.
