🇬🇧 English Version
About The Project

As an engineering student passionate about artificial intelligence and embedded systems, I developed this project to explore real-time computer vision and Edge-AI deployment.

The main goal is to build an automated monitoring system for solar panels using lightweight deep learning techniques right on the edge device without relying on external cloud processing.

Key Features & Technologies Used:

Dataset & Training: Prepared a dedicated solar panel dataset via Roboflow and trained a custom YOLOv8 segmentation model on Google Colab.

Hardware Setup: Deployed on Raspberry Pi 4 with Camera Module 3 (IMX708).

Low-Latency Camera Pipeline: Built a custom Python implementation leveraging Picamera2 and libcamera drivers to handle raw frame access efficiently.

Real-Time Segmentation: Successfully achieved live panel segmentation and target boundary detection on device.

Future Scope: Expanding the system to detect surface contamination and efficiency loss caused by soiling.

🇹🇷 Türkçe Versiyon
Proje Hakkında

Yapay zeka ve gömülü sistemler alanında kendimi geliştiren bir mühendislik öğrencisi olarak, bu projeyi gerçek zamanlı bilgisayarlı görü ve Edge-AI uygulamalarını öğrenmek amacıyla geliştirdim.

Projenin temel amacı; harici bir sunucu veya bulut sistemine ihtiyaç duymadan, doğrudan uç cihaz (edge device) üzerinde derin öğrenme modelleri çalıştırarak güneş panellerini otomatik olarak tespit ve segmente eden bir izleme sistemi kurmaktır.

Neler Kullandım ve Ne Yaptım?

Veri Seti ve Model Eğitimi: Roboflow üzerinde hazırladığım güneş paneli veri setini Google Colab ortamında YOLOv8 segmentasyon mimarisi ile eğittim.

Donanım Altyapısı: Modeli Raspberry Pi 4 ve Kamera Modülü 3 (IMX708) üzerine entegre ettim.

Düşük Gecikmeli Kamera Bağlantısı: Standart kütüphanelerin gecikmelerini aşmak için libcamera ve Picamera2 altyapısını kullanan özel bir Python betiği geliştirdim.

Gerçek Zamanlı Segmentasyon: Canlı kamera akışında güneş panellerini piksel düzeyinde segmente etmeyi başardım.

Gelecek Planı: Modeli, paneller üzerindeki kirlenme ve verim kaybını tespit edecek şekilde genişletmek.
