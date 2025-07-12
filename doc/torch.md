
这里对torch的量化工具链进行对应的介绍

qconfig 只是一个容器，用来指定“使用哪种 observer/fake quantizer”。而实际控制量化行为（如位宽、数据类型、对称性等）的，是这些 observer 自己的参数。


PyTorch 的量化设计基于以下思想：

1. “量化行为” = Observer + FakeQuantizer 的组合
量化本质上是把浮点数 → 整数（+scale + zero point）

为此，需要 观察输入的分布（observer）

然后再用 scale/zero_point 去模拟量化（FakeQuantizer）

2. qconfig 是一个“策略工厂”
python
复制
编辑
qconfig = QConfig(
    activation=MinMaxObserver.with_args(dtype=quint8, qscheme=per_tensor_affine),
    weight=PerChannelMinMaxObserver.with_args(dtype=qint8, qscheme=per_channel_symmetric)
)
你看不到 bit_width=8 之类的参数，而是通过传递给 Observer 的 dtype、qscheme 等来控制。

PyTorch 的思路是：

🔧 “想怎么量化，就选择什么 observer；qconfig 只负责告诉框架用哪个 observer。”


Observer 是用于在量化之前收集张量的统计信息（如 min/max），以便计算 scale 和 zero_point。

```shell
1. 用户定义策略
    ↓
[QConfig]               ←←←←←←←←←←←←←←←←←←←←←←
    ↓                                           ↑
2. 插入观察器（静态量化）                ↑
[Observer] ← 负责收集张量 min/max     ↑ 由 QConfig 选择何种 Observer/FakeQuant
    ↓                                           ↑
3. 生成 scale/zero_point                   ↑
    ↓                                           ↑
4. 模拟量化（仅 QAT）                →→→→→→→→→→→→→→
[FakeQuant] ← 用浮点值模拟量化影响（训练）
    ↓
5. FX 工具链插入/追踪量化逻辑
[prepare_fx → convert_fx] ← 自动插桩、替换模块
    ↓
6. 最终输出可部署量化模型
[QuantizedModel] ← 包含 INT8 Conv、Linear、ReLU等
```




