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

# 📦 版本迭代记录

# 🚀 未来计划（Roadmap）
 支持 QAT（量化感知训练）

 支持 LoRA 微调与插拔

 支持混合精度部署（INT4 + FP16）

 兼容 ONNX 与 Transformers 格式

# 📬 联系方式
如有建议、合作或问题，欢迎联系我：

📧 邮箱: njuskyrim@qq.com

📂 GitHub: [SkyQuant](https://github.com/skyrimforest/SkyQuant)

