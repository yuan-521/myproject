from ultralytics import YOLO

# 1. 加载模型（和代码在同一个文件夹，直接写文件名）
model = YOLO("yolov8n.pt")

# 2. 读取 test_images 里的原始图片（相对路径写法）
img_path = "../test_images/屏幕截图 2025-08-29 153535.png"

# 3. 运行检测，并指定保存到 yolo_result 文件夹
results = model(
    img_path,
    project="yolo_result",  # 你的结果文件夹名
    name="pig_detect",      # 每次运行的子文件夹名（可改，方便区分）
    save=True               # 开启自动保存
)

# 4. 同时弹出窗口显示结果（按任意键关闭）
results[0].show()