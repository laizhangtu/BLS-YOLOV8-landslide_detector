from ultralytics import YOLO

yolo = YOLO("E:\\code\\yolov8\\ultralytics-main\\runs\\detect\\train36\\weights\\best.pt",task="detect")# use model where

result = yolo(source="E:\code\yoloproject\datasets\Bijie-landslide-dataset\landslide\image\qxg021.png",save=True,show=True)
#result = yolo(source= ,save=True,show=True)