import cv2
from picamera2 import Picamera2
from ultralytics import YOLO

# 1. Eğitilmiş YOLOv8 modelini yükle
model = YOLO("best.pt")

# 2. IMX708 Kamera sürücüsünü Picamera2 ile başlat
picam2 = Picamera2()
config = picam2.create_preview_configuration(main={"size": (640, 480)})
picam2.configure(config)
picam2.start()

# 3. Canlı görüntü akışı ve tahmin döngüsü
try:
    while True:
        frame = picam2.capture_array()  # Anlık kareyi RAM'den al
        results = model(frame, verbose=False)  # YOLOv8 segmentasyon tahmini
        annotated_frame = results[0].plot()  # Tespitleri kare üzerine çiz
        
        cv2.imshow("Solar Panel Detection - Realtime", annotated_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    picam2.stop()
    cv2.destroyAllWindows()
