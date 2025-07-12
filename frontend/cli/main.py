'''
@Project ：SkyQuant 
@File    ：main.py
@IDE     ：PyCharm 
@Author  ：Skyrim
@Date    ：2025/7/11 10:16 
'''
# main.py

import argparse
import torch
from torchvision.models import resnet18
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

from compressor.core import Compressor
from compressor.modules.quantization import QuantizationModule
from compressor.modules.pruning import PruningModule
from compressor.modules.distillation import DistillationModule  # 可选

def parse_args():
    parser = argparse.ArgumentParser(description="神经网络压缩工具")

    parser.add_argument("--method", type=str, choices=["quant", "prune", "distill"], required=True,
                        help="压缩方法：quant / prune / distill")
    parser.add_argument("--model", type=str, default="resnet18", help="模型名称")
    parser.add_argument("--save_path", type=str, default="compressed_model.pt", help="保存路径")

    # 量化参数
    parser.add_argument("--bit", type=int, default=8, help="量化位宽（仅对量化有效）")

    # 剪枝参数
    parser.add_argument("--sparsity", type=float, default=0.3, help="剪枝稀疏度（仅对剪枝有效）")

    # 蒸馏参数（可扩展）
    parser.add_argument("--teacher_path", type=str, default=None, help="教师模型路径（仅对蒸馏有效）")

    return parser.parse_args()

def load_model(name="resnet18"):
    if name == "resnet18":
        return resnet18(pretrained=True)
    else:
        raise NotImplementedError(f"暂不支持模型: {name}")

def get_dummy_calibration_loader():
    transform = transforms.Compose([transforms.Resize(224), transforms.ToTensor()])
    dataset = datasets.FakeData(size=10, image_size=(3, 224, 224), transform=transform)
    return DataLoader(dataset, batch_size=2)

def main():
    args = parse_args()

    model = load_model(args.model)
    compressor = Compressor(model)

    if args.method == "quant":
        compressor.enable(QuantizationModule, config={"bit": args.bit})
    elif args.method == "prune":
        compressor.enable(PruningModule, config={"sparsity": args.sparsity})
    elif args.method == "distill":
        compressor.enable(DistillationModule, config={})
    else:
        raise ValueError(f"未知方法: {args.method}")

    calibration_loader = get_dummy_calibration_loader()
    compressed_model = compressor.run(calibration_data=calibration_loader)

    torch.save(compressed_model.state_dict(), args.save_path)
    print(f"✅ 模型已保存至: {args.save_path}")

if __name__ == "__main__":
    main()
