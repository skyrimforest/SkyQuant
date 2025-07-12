'''
@Project ：SkyQuant 
@File    ：torch_quant.py
@IDE     ：PyCharm 
@Author  ：Skyrim
@Date    ：2025/7/11 17:56 
'''
import torchvision
import torch
from torch.quantization.quantize_fx import prepare_fx, convert_fx
from torch.ao.quantization import get_default_qconfig, QConfigMapping

def quantize_model():

    # 1. 模型准备
    model = torchvision.models.resnet18(pretrained=True)
    model.eval()

    # 2. 配置量化策略
    qconfig_mapping = QConfigMapping().set_global(get_default_qconfig("fbgemm"))

    # 3. 插入 Observer
    example_inputs = torch.randn(1, 3, 224, 224)
    prepared = prepare_fx(model, qconfig_mapping, example_inputs)

    # 4. 用校准数据跑一遍（让 observer 收集 min/max）
    with torch.no_grad():
        prepared(example_inputs)

    # 5. 转换为量化模型
    quantized_model = convert_fx(prepared)

    # 6. 量化模型 ready，Conv/Linear 等都已替换为 INT8 实现




