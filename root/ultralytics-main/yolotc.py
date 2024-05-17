from ultralytics import YOLO

# Initialize the YOLO model
model = YOLO('/root/ultralytics-main/runs/detect/train7/weights/best.pt')

# Tune hyperparameters on COCO8 for 30 epochs
model.tune(data='/root/ultralytics-main/yolo-ls.yaml', epochs=100, iterations=300, optimizer='AdamW', plots=False, save=False, val=False)