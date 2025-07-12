# 🧠 SkyQuant  - 简单高效的神经网络压缩工具
这是一个轻量化的神经网络模型压缩工具，旨在帮助开发者、研究人员和部署工程师以最小的代价对深度学习模型进行压缩优化，便于在资源受限的环境中运行。

本项目将持续扩展和优化，逐步支持更多压缩策略与模型类型，最终成为一个统一的压缩工具平台。

# ✅ 当前支持功能
✔️ 权重量化（Weight Quantization）

✔️ 激活量化（Activation Quantization）

✔️ 简单剪枝（Pruning by Magnitude）

✔️ 模型大小评估与对比

✔️ 精度评估（Top-1 Accuracy）

✔️ PyTorch 模型支持

| 类型 | 工具                       | 简介                   |
| -- | ------------------------ | -------------------- |
| 量化 | AutoGPTQ / GPTQ          | INT4 推理              |
| 混合 | BitsAndBytes             | FP16, INT8 混合精度训练与推理 |
| 剪枝 | PyTorch-NNI / SparseML   | 支持剪枝、量化、蒸馏           |
| 蒸馏 | Huggingface Transformers | 有现成蒸馏工具              |
| 部署 | llama.cpp / vLLM         | 支持量化模型部署             |

📌 当前支持以静态图形式（如 ONNX）导出的 PyTorch 模型进行后处理压缩


# 🎮 当前支持模型

以下模型经过测试，可以实现全流程压缩。

| 类别        | 模型名                  | 描述             |
| --------- | -------------------- | -------------- |
| 🧠 图像分类   | `MobileNetV2/V3`     | 轻量级网络，适合嵌入式    |
|           | `EfficientNet`       | 精度高，结构复杂，但适合剪枝 |
|           | `ResNet18/34`        | 教育界/工业界常见标准网络  |
| 🧠 目标检测   | `YOLOv5`             | 非常主流，适合剪枝 + 量化 |
|           | `YOLOv8`             | 最新版本，兼容 ONNX   |
|           | `NanoDet`            | 极致轻量化检测网络      |
| 📈 语义分割   | `DeepLabV3`          | 嵌入式也会使用，参数可控制  |
| 📊 时序预测   | `LSTM`, `TCN`, `GRU` | 用于轨迹/控制/风速预测等  |
| 🎮 控制策略网络 | 自定义 MLP/ConvNet      | 模拟飞控/路径规划输出    |

大模型：

| 类别      | 模型名                      | 描述                    |
| ------- | ------------------------ | --------------------- |
| 📚 文本生成 | `LLaMA2` (7B/13B)        | 开源 LLM，支持 GPTQ/LoRA   |
|         | `Qwen1.5`                | 通用能力强，中文更好            |
|         | `ChatGLM2/3`             | 中文 LLM，可蒸馏量化          |
|         | `TinyLLaMA`              | 1.1B 小型模型，适合端部署       |
| 🤖 多模态  | `MiniGPT-4`              | 支持图文输入，可压缩视觉 backbone |
| 🔍 文本分类 | `BERT`, `TinyBERT`       | 支持蒸馏/剪枝/量化            |
| 📈 时间序列 | `Informer`, `Autoformer` | 长时间建模，适合低频遥测压缩预测      |


# 📦 版本迭代记录

2025/07/11 对ResNet、Yolo v5和Qwen1.5实现量化操作,打通工具全流程。


# 🚀 未来计划（Roadmap）
 支持 QAT（量化感知训练）

 支持 LoRA 微调与插拔

 支持混合精度部署（INT4 + FP16）

 兼容 ONNX 与 Transformers 格式

# 📬 联系方式
如有建议、合作或问题，欢迎联系我：

📧 邮箱: njuskyrim@qq.com

📂 GitHub: [SkyQuant](https://github.com/skyrimforest/SkyQuant)

