# oop-pong-game
Python Turtle modülü ile OOP prensiplerine uygun olarak geliştirilmiş, Q/E tuşları ile dinamik hız kontrollü Pong oyunu.

Bu proje, Python'ın `turtle` modülü kullanılarak Nesne Yönelimli Programlama (OOP) prensiplerine uygun, tamamen modüler bir mimariyle geliştirilmiş klasik bir Pong (Masa Tenisi) oyunudur.

##  Öne Çıkan Özellikler
- **Modüler Tasarım:** Oyun mimarisi; ana döngü, raketler, top ve skor tablosu olmak üzere bağımsız sınıflara (class) ayrılmıştır.
- **Dinamik Hız Kontrolü:** Standart Pong oyunlarından farklı olarak, oyuncular oyun esnasında topun hızını manuel olarak manipüle edebilirler.
- **Performans Optimizasyonu:** Python'ın bytecode (`__pycache__`) üretim mekanizması kod seviyesinde sınırlandırılarak klasör düzeni temiz tutulmuştur.

## Oyun Kontrolleri
- **Sol Oyuncu:** `W` (Yukarı) , `S` (Aşağı)
- **Sağ Oyuncu:** `Yukarı Ok` (Yukarı) , `Aşağı Ok` (Aşağı)
- **Hız Ayarları :** `Q` (Topu Hızlandır) , `E` (Topu Yavaşlat)

##  Gereksinimler ve Çalıştırma
Proje sadece Python'ın yerleşik kütüphanelerini kullandığı için harici hiçbir paket kurulumuna (`pip`) ihtiyaç duymaz.

Projeyi çalıştırmak için main.py dosyasını terminalde çalıştırmak yeterlidir.
