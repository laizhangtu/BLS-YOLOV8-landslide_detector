from ultralytics import YOLO

model = YOLO('ultralytics-main/ultralytics/cfg/models/v8/yolov8s-spd.yaml').load("E:\\code\\yolov8\\ultralytics-main\\runs\detect\\train32\\weights\\best.pt")

model.train(data= r'E:\code\yolov8\ultralytics-main\ultralytics-main\yolo-ls.yaml', workers=0, epochs=100, batch=4,optimizer="AdamW")

#v1.0 优化器变为Lion
#v1.1 加入gold-yolo模块----3.28 
#v1.2 改善Iou_loss 改为WIou_loss----3.28====暂时DEL----3.29
#v1.4 发现问题出现在数据集上，转换脚本出错，框的位置发生偏移，导致精度太低----3.30