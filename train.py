#训练模型
from ultralytics import YOLO

model = YOLO('yolo11n.pt')#使用yolov11

results = model.train(data='wheat.yaml', epochs=100, imgsz=640, batch=16, workers=0)
