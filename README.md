# 项目介绍

    本项目是针对于山体滑坡检测所开发的
    基于ultralytics公司开发的yolov8，结合gold-yolo网络，EMA网络，Wiou损失函数等，着手于山体滑坡的检测并开发了webgui界面。

本项目各结构来源
    [ultralytics](https://github.com/ultralytics/ultralytics)
    [Efficient Multi-Scale Attention Module with Cross-Spatial Learning](https://arxiv.org/abs/2305.13563v1)
    [Wise-IoU: Bounding Box Regression Loss with Dynamic Focusing Mechanism](https://arxiv.org/abs/2301.10051)
    [Gold-yolo](https://github.com/huawei-noah/Efficient-Computing/tree/master/Detection/Gold-YOLO)

# 目录结构          
    ├── MSLD_datasets                   // 测试数据
    |   └─ test
    ├── Sourcecode                      // 源代码
    |   ├── BLS-YOLO.onnx               // onnx模型
    |   ├── index.html                  // webgui
    |   ├── landslide_detector.py       
    |   └── requirements.txt
    ├── BLS-YOLO.onnx                   // 依赖文件
    ├── index.html                      
    └── landslide_detector.exe          // 执行程序

# 使用说明

    双击exe
    弹出网页
    选择文件
    等待结果

# 模型训练
    本项目可运行在
        系统： Ubuntu 18.04 
        GPU： RTX 4090(24GB)
        GPU驱动： 535.129.03
        CUDA版本： ≤ 12.2
        CPU： 16 vCPU Intel(R) Xeon(R) Platinum 8352V CPU @ 2.10GHz
        内存： 120GB
数据集来源 
    [武汉大学毕节市滑坡数据集](http://gpcv.whu.edu.cn/data/Bijie_pages.html)
    [多尺度滑坡数据集](https://github.com/YhQIAO/LandSlide_Detection_Faster-RCNN)
    
 
# Q&A

    Q: 网页未弹出
    A: 请手动自行打开 http://localhost:8080 使用任何浏览器均可 请勿关闭程序

    若有其他问题或BUG请提交 issue 或 发送邮件至 lian_zetao@foxmail.com

# 协议
    本项目遵守 AGPL-3.0协议
