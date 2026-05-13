from ultralytics import YOLO

# 加载本地模型
model = YOLO("yolov8n.pt")

# 用图片的真实路径和文件名
img_path = "../test_images/小鞠.jpg"

# 运行检测，并设置保存参数
results = model(
    img_path,
    project="yolo_result",  # 根文件夹，所有结果都在这里
    name="小鞠_detect",     # 这次的子文件夹名，区分不同图片
    save=True              # 开启自动保存
)

# 显示结果
results[0].show()