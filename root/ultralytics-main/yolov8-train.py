from ultralytics import YOLO

model = YOLO('/root/ultralytics-main/ultralytics/cfg/models/v8/yolov8.yaml').load("yolov8n.pt")

model.train(data= r'/root/ultralytics-main/yolo-ls.yaml', workers=16, epochs=200, batch=32,optimizer="AdamW")

#v1.0 优化器变为Lion----del
#v1.1 加入gold-yolo模块----3.28 
#v1.2 改善Iou_loss 改为WIou_loss----3.28====DEL----3.29===添加----4.4
#v1.4 发现问题出现在数据集上，转换脚本出错，框的位置发生偏移，导致精度太低----3.30