from ultralytics import YOLO

model = YOLO('/root/ultralytics-main/ultralytics/cfg/models/v8/yolov8.yaml').load("yolov8n.pt")

model.train(data= r'/root/ultralytics-main/yolo-ls.yaml', workers=8, epochs=150, batch=64,optimizer="AdamW")