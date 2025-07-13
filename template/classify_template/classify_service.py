'''
@Project ：SkyQuant 
@File    ：classify_service.py
@IDE     ：PyCharm 
@Author  ：Skyrim
@Date    ：2025/7/13 10:57 
'''
import torch
import torch.nn as nn
import torch.nn.functional as F
from PIL import Image
from io import BytesIO
import torchvision.transforms as transforms

import sky_config
from network.resnet import resnet_loader

def run_inference(image_file):
    # 1. 加载模型
    model = resnet_loader.get_digit_infer_model()
    # 2. 读取并预处理图像
    image = Image.open(BytesIO(image_file)).convert("RGB")
    # 👇 模拟把字符串变成特征（实际场景可改成 tokenizer、图像处理等）
    x = torch.randn(1, 10)

    # 3. 图像转换（根据模型需求调整）
    transform = transforms.Compose([
        transforms.Resize((224, 224)),  # 调整图像大小
        transforms.ToTensor(),  # 转换为张量
        transforms.Normalize(  # 归一化
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        ),
    ])

    # 4. 应用转换
    x = transform(image).unsqueeze(0)  # 添加批次维度

    # 5. 模型推理
    with torch.no_grad():
        logits = model(x)
        probs = F.softmax(logits, dim=1).squeeze().tolist()
        pred = int(torch.argmax(logits, dim=1).item())

    return probs, pred



