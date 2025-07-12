'''
@Project ：SkyQuant 
@File    ：setting.py
@IDE     ：PyCharm 
@Author  ：Skyrim
@Date    ：2025/7/12 13:19 
'''

from enum import Enum, auto


class TaskType(Enum):
    """任务类型枚举"""
    # 视觉类型
    IMAGE_CLASSIFICATION = 100

    # LLM
    TEXT_CLASSIFICATION = 200

    # 测试
    OTHER = 999


class TargetPlatform(Enum):
    """目标平台枚举"""
    ARM_MOBILE = 1
    X86_SERVER = 2
    NVIDIA_GPU = 3
    ASCEND_NPU = 4
    CAMBRICON_MLU = 5
    FPGA = 6
    CPU_GENERIC = 7


class Priority(Enum):
    """优化优先级枚举"""
    BALANCED = 10  # 平衡

    ACCURACY = 20  # 精度

    LATENCY = 30  # 时延

    THROUGHPUT = auto()  # 优先吞吐量
    ENERGY_EFFICIENCY = auto()  # 优先能效


class ModelType(Enum):
    """模型类型枚举"""
    CNN = 100
    TRANSFORMER = 200
    HYBRID = 999
