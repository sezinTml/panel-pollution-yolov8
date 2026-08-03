# ☀️ Real-Time Solar Panel Segmentation on Edge-AI

---

### 🇬🇧 English Version

#### 📌 About The Project
As an engineering student passionate about artificial intelligence and embedded systems, I developed this project to explore real-time computer vision and Edge-AI deployment. 

The main goal is to build an automated monitoring system for solar panels using lightweight deep learning techniques right on the edge device without relying on external cloud processing.

#### 🛠️ Key Features & Technologies Used
* **Dataset & Training:** Prepared a dedicated solar panel dataset via Roboflow and trained a custom YOLOv8 segmentation model on Google Colab.
* **Hardware Setup:** Deployed on Raspberry Pi with Camera Module 3 (IMX708).
* **Low-Latency Camera Pipeline:** Built a custom Python implementation leveraging `Picamera2` and `libcamera` drivers to handle raw frame access efficiently.
* **Real-Time Segmentation:** Successfully achieved live panel segmentation and target boundary detection on device.

*Future Scope: Expanding the system to detect surface contamination and efficiency loss caused by soiling.*

---

### 🇹🇷 Türkçe Versiyon

#### 📌 Proje Hakkında
Yapay zeka ve gömülü sistemler alanında kendimi geliştiren bir mühendislik öğrencisi olarak, bu projeyi gerçek zamanlı bilgisayarlı görü ve Edge-AI uygulamalarını öğrenmek amacıyla geliştirdim.

Projenin temel amacı; harici bir sunucu veya bulut sistemine ihtiyaç duymadan, doğrudan uç cihaz (edge device) üzerinde derin öğrenme modelleri çalıştırarak güneş panellerini otomatik olarak tespit ve segmente eden bir izleme sistemi kurmaktır.

#### 🛠️ Neler Kullandım ve Ne Yaptım?
* **Veri Seti ve Model Eğitimi:** Roboflow üzerinde hazırladığım güneş paneli veri setini Google Colab ortamında YOLOv8 segmentasyon mimarisi ile eğittim.
* **Donanım Altyapısı:** Modeli Raspberry Pi ve Kamera Modülü 3 (IMX708) üzerine entegre ettim.
* **Düşük Gecikmeli Kamera Bağlantısı:** Standart kütüphanelerin gecikmelerini aşmak için `libcamera` ve `Picamera2` altyapısını kullanan özel bir Python betiği geliştirdim.
* **Gerçek Zamanlı Segmentasyon:** Canlı kamera akışında güneş panellerini piksel düzeyinde segmente etmeyi başardım.

*Gelecek Planı: Modeli, paneller üzerindeki kirlenme ve verim kaybını tespit edecek şekilde genişletmek.*

---

## ⚙️ Setup & Deployment (Raspberry Pi Environment)

To isolate system dependencies on Raspberry Pi OS (Bookworm) and enable access to native `libcamera` drivers:

```bash
# 1. Create and activate virtual environment
python -m venv myenv
source ~/myenv/bin/activate

# 2. Install required dependencies
pip install ultralytics opencv-python picamera2

# 3. Grant system site-packages access for libcamera integration
sed -i 's/include-system-site-packages = false/include-system-site-packages = true/' ~/myenv/pyvenv.cfg


## 🚀 How to Run / Çalıştırma

1. Open terminal and navigate to project directory / Proje dizinine git:
   ```bash
   cd ~/İndirilenler  # Ya da kodlarının olduğu klasör
2. Activate virtual environment / Sanal ortamı aktifleştir:
   ```bash
   source ~/myenv/bin/activate
3. Run live inference script / Canlı tespit betiğini çalıştır:
   ```bash
   python live_yolo.py
4. Press q on the display screen or Ctrl + C in terminal to exit.

💻 Tech Stack

Hardware: Raspberry Pi 4, Camera Module 3 (IMX708)
Software & Libraries: Python 3, YOLOv8 (Ultralytics), OpenCV, Picamera2, libcamera, Roboflow, Google Colab
