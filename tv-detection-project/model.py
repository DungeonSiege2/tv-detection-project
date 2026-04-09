from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

def detect_tv(image_path):
    results = model(image_path)

    image = cv2.imread(image_path)
    count = 0

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])

            if model.names[cls] == "tv":
                count += 1

                # координаты рамки
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # рисуем прямоугольник
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

                # подпись
                cv2.putText(image, "TV", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # сохраняем обработанное изображение
    output_path = image_path.replace(".", "_result.")
    cv2.imwrite(output_path, image)

    return count, output_path