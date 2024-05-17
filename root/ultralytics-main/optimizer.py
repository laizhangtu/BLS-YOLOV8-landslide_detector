import torch.optim as optim

# 初始化模型
model = YOLOv8()

# 设置初始学习率
initial_learning_rate = 0.0001

# 定义优化器
optimizer = optim.Adam(model.parameters(), lr=initial_learning_rate)